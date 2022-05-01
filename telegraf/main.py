from orwell import Metric, Runner


title_mappings = {
  'memory_total': 'node_memory_MemTotal_bytes',
  'memory_free': 'node_memory_MemFree_bytes',
  'memory_available': 'node_memory_MemAvailable_bytes',
  'memory_cached': 'node_memory_Cached_bytes',
  'memory_buffered': 'node_memory_Buffers_bytes',
  'swap_total': 'node_memory_SwapTotal_bytes',
  'swap_free': 'node_memory_SwapFree_bytes',
  'system_uptime': 'node_time_seconds',
}

def translate (line: str) -> list:
  if len(line.strip()) == 0: return []
  if line.startswith("> "): line = line[2:]
  properties, metrics, ts = line.split(" ")

  properties = properties.split(",")
  title = properties[0]
  properties = { prop: value for prop, value in [prop.split('=') for prop in properties[1:]] }

  metrics = [metric.split('=') for metric in metrics.split(',')]

  return [ create_metric(title + '_' + metric, value, properties, ts) for metric, value in metrics ]


def create_metric (title: str, value: str, properties: dict, ts: str) -> Metric:
  if title.startswith('cpu_time_'):
    properties = { 'cpu': properties['cpu'].strip('cpu'), 'mode': title.split('_')[-1] }
    title = 'node_cpu_seconds_total'

  elif title.startswith('system_load'):
    title = title.replace('system_load', 'node_load')

  if title in title_mappings.keys():
    title = title_mappings[title]
    
  return Metric(title, value, properties, ts)




translator = Runner(translate)
translator.run()
