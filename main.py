from flask import Flask, request, make_response
from kafka import KafkaConsumer, errors
from redis import Redis

from time import time
from sys import argv, stderr


TIMESTAMP_LENGTH = 13


class Metric:

  def __init__ (self, title: str, value: str, properties: dict = {}, timestamp: float = None):
    self._title = title
    self._value = value
    self._properties = properties
    self._timestamp = time() if timestamp is None else timestamp

    self._str_cache = None

  @property
  def title (self): 
    return self._title

  @property
  def value (self): 
    return self._value

  @property
  def properties (self): 
    return self._properties

  @property
  def timestamp (self): 
    return self._timestamp

  def __str__(self) -> str:
    if self._str_cache is None:
      value = self.value.replace('i', '')

      properties = ','.join(['%s="%s"' % (prop, value) for prop, value in self.properties.items()])

      timestamp = str(self.timestamp)[:TIMESTAMP_LENGTH]
      timestamp += ''.join(['0' for _ in range(TIMESTAMP_LENGTH-len(timestamp))])

      self._str_cache = "%s{%s} %s %s" % (self._title, properties, value, timestamp)

    return self._str_cache


def concatenate_metrics (metrics: list) -> str:
  return '\n'.join([ concatenate_metrics(metric) if type(metric) == list else str(metric) for metric in metrics ])


def serve (translation_function: callable, host="localhost", debug=False, port=5000):
  app = Flask(__name__)

  @app.route('/metrics')
  def metrics ():
    data = request.get_json(True, True)

    if not data or 'metrics' not in data.keys():
      response = make_response('', 400)
    
    else:
      response = concatenate_metrics(list(map(translation_function, [ line for line in data['metrics'].split('\n') if line ])))
      response = make_response(response, 200)

    response.mimetype="text/plain"
    return response

  app.run(host=host, port=port, debug=debug)


def prod (translation_function: callable):
  def consume (metrics: list[Metric]):
    conn = Redis(password="root")
    pipe = conn.pipeline()

    for metric in metrics: pipe.set(metric.title, metric.value)

    pipe.execute()
    conn.close()

  consumer = KafkaConsumer('telegraf', bootstrap_servers=[ 'localhost:9092' ], value_deserializer=lambda m: list(map(translation_function, m.decode('ascii').split('\n'))))
  
  for msg in consumer: 
    for batch in msg.value: 
      consume(batch)


def translate (line: str) -> Metric | list[Metric]:
  properties, metrics, ts = line[2:].split(" ")

  properties = properties.split(",")
  title = properties[0]
  properties = { prop: value for prop, value in [prop.split('=') for prop in properties[1:]] }

  metrics = [metric.split('=') for metric in metrics.split(',')]

  return [ Metric(title + '_' + metric, value, properties, ts) for metric, value in metrics ]


def main ():

  CMD_TEXT = 'cmd'
  SERVER_TEXT = 'server'
  PROD_TEXT = 'prod'

  RUN_MODES = [ CMD_TEXT, SERVER_TEXT, PROD_TEXT ]

  if len(argv) < 2 or argv[1] not in RUN_MODES:
    print("Run mode not recognised!\nUsage: python " + __file__ + " <run_mode> [OPTIONS]\nAvailable modes: " + ", ".join(RUN_MODES), file=stderr)

  elif argv[1] == CMD_TEXT:
    print(concatenate_metrics(translate(argv[2])))

  elif argv[1] == SERVER_TEXT:
    serve(translate, debug=True)

  elif argv[1] == PROD_TEXT:
    prod(translate)


if __name__ == '__main__':
  main()