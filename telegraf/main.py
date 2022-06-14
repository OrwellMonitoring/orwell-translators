from orwell import Metric, Runner, MetricsFactory


def translate (line: str) -> list:
  if len(line.strip()) == 0: return []
  if line.startswith("> "): line = line[2:]
  properties, metrics, ts = line.split(" ")

  properties = properties.split(",")
  title = properties[0]
  properties = { prop: value for prop, value in [prop.split('=') for prop in properties[1:]] }

  metrics = [metric.split('=') for metric in metrics.split(',')]

  result = []
  for metric, value in metrics: 
    data = create_metric(title + '_' + metric, value, properties, ts)
    data = data if type(data) == list else [data]
    for d in data: d._properties['instance'] = properties['instance']
    result += data
  return result


def create_metric (title: str, value: str, properties: dict, ts: str) -> Metric:
  if title.startswith('cpu_time_'): return MetricsFactory.create_cpu_time_metric(properties['cpu'].strip('cpu'), title.split('_')[-1], value, ts, properties['instance'])

  elif title == 'memory_commit_limit': return MetricsFactory.create_memory_commit_limit_metric(value, ts, properties['instance'])
  elif title == 'memory_committed_as': return MetricsFactory.create_memory_committed_as_metric(value, ts, properties['instance'])

  elif title == 'memory_vmalloc_total': return MetricsFactory.create_memory_vmalloc_total_metric(value, ts, properties['instance'])
  elif title == 'memory_vmalloc_chunk': return MetricsFactory.create_memory_vmalloc_chunk_metric(value, ts, properties['instance'])
  elif title == 'memory_vmalloc_used': return MetricsFactory.create_memory_vmalloc_used_metric(value, ts, properties['instance'])

  elif title == 'memory_huge_pages_total': return MetricsFactory.create_memory_huge_pages_metric(value, ts, properties['instance'])
  elif title == 'memory_huge_pages_free': return MetricsFactory.create_memory_huge_pages_free_metric(value, ts, properties['instance'])
  elif title == 'memory_huge_page_size': return MetricsFactory.create_memory_huge_pages_size_metric(value, ts, properties['instance'])

  elif title == 'memory_swap_free': return MetricsFactory.create_memory_swap_free_metric(value, ts, properties['instance'])
  elif title == 'memory_swap_total': return MetricsFactory.create_memory_swap_total_metric(value, ts, properties['instance'])

  elif title == 'memory_write_back': return MetricsFactory.create_memory_writeback_metric(value, ts, properties['instance'])
  elif title == 'memory_write_back_tmp': return MetricsFactory.create_memory_writeback_tmp_metric(value, ts, properties['instance'])

  elif title == 'memory_dirty': return MetricsFactory.create_memory_dirty_metric(value, ts, properties['instance'])
  elif title == 'memory_free': return MetricsFactory.create_memory_free_metric(value, ts, properties['instance'])
  elif title == 'memory_available': return MetricsFactory.create_memory_available_metric(value, ts, properties['instance'])
  elif title == 'memory_inactive': return MetricsFactory.create_memory_inactive_metric(value, ts, properties['instance'])
  elif title == 'memory_total': return MetricsFactory.create_memory_total_metric(value, ts, properties['instance'])
  elif title == 'memory_mapped': return MetricsFactory.create_memory_mapped_metric(value, ts, properties['instance'])
  elif title == 'memory_page_tables': return MetricsFactory.create_memory_page_tables_metric(value, ts, properties['instance'])
  elif title == 'memory_cached': return MetricsFactory.create_memory_cached_metric(value, ts, properties['instance'])
  elif title == 'memory_slab': return MetricsFactory.create_memory_slab_metric(value, ts, properties['instance'])
  elif title == 'memory_sreclaimable': return MetricsFactory.create_memory_reclaimable_metric(value, ts, properties['instance'])
  elif title == 'memory_active': return MetricsFactory.create_memory_active_metric(value, ts, properties['instance'])

  elif title == 'disk_total': return MetricsFactory.create_filesystem_size_metric(properties['device'], properties['fstype'], properties['path'], value, ts, properties['instance'])
  elif title == 'disk_free': return MetricsFactory.create_filesystem_available_metric(properties['device'], properties['fstype'], properties['path'], value, ts, properties['instance'])
  
  elif title == 'diskio_write_bytes': return MetricsFactory.create_disk_read_bytes_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_read_bytes': return MetricsFactory.create_disk_written_bytes_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_reads': return MetricsFactory.create_disk_reads_completed_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_writes': return MetricsFactory.create_disk_writes_completed_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_io_time': return MetricsFactory.create_disk_io_time_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_write_time': return MetricsFactory.create_disk_io_write_time_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_read_time': return MetricsFactory.create_disk_io_read_time_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_weighted_io_time': return MetricsFactory.create_disk_io_time_weighted_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_merged_reads': return MetricsFactory.create_disk_io_reads_merged_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_merged_writes': return MetricsFactory.create_disk_io_writes_merged_metric(properties['name'], value, ts, properties['instance'])
  elif title == 'diskio_iops_in_progress': return MetricsFactory.create_disk_io_now_metric(properties['name'], value, ts, properties['instance'])

  elif title == 'net_bytes_recv': return MetricsFactory.create_network_receive_bytes_metric(value, ts, properties['instance'])
  elif title == 'net_bytes_sent': return MetricsFactory.create_network_transmit_bytes_metric(value, ts, properties['instance'])

  elif title == 'system_uptime': return [ MetricsFactory.create_up_time_metric(value, ts, properties['instance']), MetricsFactory.create_boot_time_metric('0', ts, properties['instance']) ]

  elif title == 'system_load5': return MetricsFactory.create_load_metric(5, value, ts, properties['instance'])
  elif title == 'system_load15': return MetricsFactory.create_load_metric(15, value, ts, properties['instance'])

  return []
  
 
translator = Runner(translate)
translator.run()
