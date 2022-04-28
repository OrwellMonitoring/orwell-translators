from orwell import Metric, Runner


def translate (line: str) -> list:
  if line.startswith("> "): line = line[2:]
  properties, metrics, ts = line.split(" ")

  properties = properties.split(",")
  title = properties[0]
  properties = { prop: value for prop, value in [prop.split('=') for prop in properties[1:]] }

  metrics = [metric.split('=') for metric in metrics.split(',')]

  return [ Metric(title + '_' + metric, value, properties, ts) for metric, value in metrics ]


translator = Runner(translate)
translator.run()