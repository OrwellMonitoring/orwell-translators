from orwell import Metric, Runner


class MetricsFactory:

  @classmethod
  def create_load_metric (cls, interval: int, value: str, ts: str):
    return Metric('node_load' + str(interval), value, { }, ts)

  @classmethod
  def create_cpu_time_metric (cls, cpu: str, mode: str, value: str, ts: str):
    return Metric('node_cpu_seconds_total', value, { 'cpu': cpu, 'mode': mode }, ts)

  @classmethod
  def create_filesystem_metric (cls, title: str, device: str, fstype: str, mountpoint: str, value: str, ts: str):
    return Metric('node_filesystem_%s_bytes' % (title,), value, { 'device': device, 'fstype': fstype, 'mountpoint': mountpoint }, ts)

  @classmethod
  def create_filesystem_available_metric (cls, device: str, fstype: str, mountpoint: str, value: str, ts: str):
    return cls.create_filesystem_metric('avail', device, fstype, mountpoint, value, ts)

  @classmethod
  def create_filesystem_size_metric (cls, device: str, fstype: str, mountpoint: str, value: str, ts: str):
    return cls.create_filesystem_metric('size', device, fstype, mountpoint, value, ts)

  @classmethod
  def create_memory_metric (cls, title: str, value: str, ts: str):
    return Metric('node_memory_%s_bytes' % (title,), value, {  }, ts)

  @classmethod
  def create_memory_total_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('MemTotal', value, ts)

  @classmethod
  def create_memory_free_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('MemFree', value, ts)

  @classmethod
  def create_memory_available_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('MemAvailable', value, ts)

  @classmethod
  def create_memory_cached_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Cached', value, ts)

  @classmethod
  def create_memory_cached_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Buffers', value, ts)

  @classmethod
  def create_memory_slab_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Slab', value, ts)

  @classmethod
  def create_memory_bounce_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Bounce', value, ts)

  @classmethod
  def create_memory_page_tables_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('PageTables', value, ts)

  @classmethod
  def create_memory_inactive_metric (cls, value: str, ts: str, detail: str = None):
    return cls.create_memory_metric('Inactive%s' % ('' if detail is None else '_' + detail,), value, ts)

  @classmethod
  def create_memory_inactive_file_metric (cls, value: str, ts: str):
    return cls.create_memory_inactive_metric(value, ts, 'file')

  @classmethod
  def create_memory_inactive_anon_metric (cls, value: str, ts: str):
    return cls.create_memory_inactive_metric(value, ts, 'anon')

  @classmethod
  def create_memory_active_metric (cls, value: str, ts: str, detail: str = None):
    return cls.create_memory_metric('Active%s' % ('' if detail is None else '_' + detail,), value, ts)

  @classmethod
  def create_memory_active_anon_metric (cls, value: str, ts: str):
    return cls.create_memory_active_metric(value, ts, 'anon')

  @classmethod
  def create_memory_committed_as_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Committed_AS', value, ts)

  @classmethod
  def create_memory_commit_limit_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('CommitLimit', value, ts)

  @classmethod
  def create_memory_swap_metric (cls, title: str, value: str, ts: str):
    return cls.create_memory_metric('Swap%s' % (title,), value, ts)

  @classmethod
  def create_memory_swap_total_metric (cls, value: str, ts: str):
    return cls.create_memory_swap_metric('Total', value, ts)

  @classmethod
  def create_memory_swap_free_metric (cls, value: str, ts: str):
    return cls.create_memory_swap_metric('Free', value, ts)

  @classmethod
  def create_memory_vmalloc_metric (cls, title: str, value: str, ts: str):
    return cls.create_memory_metric('Vmalloc%s' % (title,), value, ts)

  @classmethod
  def create_memory_vmalloc_chunk_metric (cls, value: str, ts: str):
    return cls.create_memory_vmalloc_metric('Chunk', value, ts)

  @classmethod
  def create_memory_vmalloc_total_metric (cls, value: str, ts: str):
    return cls.create_memory_vmalloc_metric('Total', value, ts)

  @classmethod
  def create_memory_vmalloc_used_metric (cls, value: str, ts: str):
    return cls.create_memory_vmalloc_metric('Used', value, ts)

  @classmethod
  def create_memory_writeback_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Writeback', value, ts)

  @classmethod
  def create_memory_writeback_tmp_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('WritebackTmp', value, ts)

  @classmethod
  def create_memory_dirty_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Dirty', value, ts)

  @classmethod
  def create_memory_mapped_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Mapped', value, ts)

  @classmethod
  def create_memory_shmem_metric (cls, value: str, ts: str, detail: str = None):
    return cls.create_memory_metric('Shmem%s' % ('' if detail is None else '_' + detail,), value, ts)

  @classmethod
  def create_memory_shmem_huge_pages_metric (cls, value: str, ts: str):
    return cls.create_memory_shmem_metric(value, ts, 'HugePages')

  @classmethod
  def create_memory_shmem_pmd_mapped_metric (cls, value: str, ts: str):
    return cls.create_memory_shmem_metric(value, ts, 'PmdMapped')

  @classmethod
  def create_memory_unreclaim_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('SUnreclaim', value, ts)

  @classmethod
  def create_memory_reclaimable_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('SReclaimable', value, ts)

  @classmethod
  def create_memory_anon_metric (cls, value: str, ts: str, detail: str = None):
    return cls.create_memory_metric('Anon%s' % ('' if detail is None else '_' + detail,), value, ts)

  @classmethod
  def create_memory_anon_huge_pages_metric (cls, value: str, ts: str):
    return cls.create_memory_anon_metric(value, ts, 'HugePages')

  @classmethod
  def create_memory_anon_pages_metric (cls, value: str, ts: str):
    return cls.create_memory_anon_metric(value, ts, 'Pages')

  @classmethod
  def create_memory_kernel_stack_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('KernelStack', value, ts)

  @classmethod
  def create_memory_percpu_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Percpu', value, ts)

  @classmethod
  def create_memory_huge_pages_metric (cls, value: str, ts: str, detail: str = None):
    return Metric('node_memory_HugePages_%s' % ('' if detail is None else '_' + detail,), value, {}, ts)

  @classmethod
  def create_memory_huge_pages_free_metric (cls, value: str, ts: str):
    return cls.create_memory_huge_pages_metric(value, ts, 'Free')

  @classmethod
  def create_memory_huge_pages_rsvd_metric (cls, value: str, ts: str):
    return cls.create_memory_huge_pages_metric(value, ts, 'Rsvd')

  @classmethod
  def create_memory_huge_pages_total_metric (cls, value: str, ts: str):
    return cls.create_memory_huge_pages_metric(value, ts, 'Total')

  @classmethod
  def create_memory_direct_map_metric (cls, value: str, ts: str, detail: str = None):
    return cls.create_memory_metric('DirectMap%s' % ('' if detail is None else '_' + detail,), value, ts)

  @classmethod
  def create_memory_direct_map_1g_metric (cls, value: str, ts: str):
    return cls.create_memory_direct_map_metric(value, ts, '1G')

  @classmethod
  def create_memory_direct_map_2m_metric (cls, value: str, ts: str):
    return cls.create_memory_direct_map_metric(value, ts, '2M')

  @classmethod
  def create_memory_direct_map_4k_metric (cls, value: str, ts: str):
    return cls.create_memory_direct_map_metric(value, ts, '4k')

  @classmethod
  def create_memory_huge_pages_free_metric (cls, value: str, ts: str):
    return cls.create_memory_huge_pages_metric(value, ts, 'Free')

  @classmethod
  def create_memory_huge_pages_rsvd_metric (cls, value: str, ts: str):
    return cls.create_memory_huge_pages_metric(value, ts, 'Rsvd')

  @classmethod
  def create_memory_huge_pages_total_metric (cls, value: str, ts: str):
    return cls.create_memory_huge_pages_metric(value, ts, 'Total')

  @classmethod
  def create_memory_huge_pages_size_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Hugepagesize', value, ts)

  @classmethod
  def create_memory_unevictable_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Unevictable', value, ts)

  @classmethod
  def create_memory_mlocked_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('Mlocked', value, ts)

  @classmethod
  def create_memory_nfs_metric (cls, value: str, ts: str):
    return cls.create_memory_metric('NFS_Unstable', value, ts)

  @classmethod
  def create_up_time_metric (cls, value: str, ts: str):
    return Metric('node_time_seconds', value, {  }, ts)

  @classmethod
  def create_boot_time_metric (cls, value: str, ts: str):
    return Metric('node_boot_time_seconds', value, {  }, ts)

  @classmethod
  def create_network_bytes_metric (cls, title: str, value: str, ts: str):
    return Metric('node_network_%s_bytes_total' % (title,), value, {  }, ts)

  @classmethod
  def create_network_receive_bytes_metric (cls, value: str, ts: str):
    return cls.create_network_bytes_metric('receive', value, ts)

  @classmethod
  def create_network_transmit_bytes_metric (cls, value: str, ts: str):
    return cls.create_network_bytes_metric('transmit', value, ts)

  @classmethod
  def create_disk_metric (cls, title: str, device: str, value: str, ts: str):
    return Metric('node_disk_%s_total' % (title,), value, { 'device': device }, ts)

  @classmethod
  def create_disk_completed_metric (cls, title: str, device: str, value: str, ts: str):
    return cls.create_disk_metric('%s_completed' % (title,), device, value, ts)

  @classmethod
  def create_disk_reads_completed_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_completed_metric('reads', device, value, ts)

  @classmethod
  def create_disk_writes_completed_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_completed_metric('writes', device, value, ts)

  @classmethod
  def create_disk_bytes_metric (cls, title: str, device: str, value: str, ts: str):
    return cls.create_disk_metric('%s_bytes' % (title,), device, value, ts)

  @classmethod
  def create_disk_read_bytes_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_bytes_metric('read', device, value, ts)

  @classmethod
  def create_disk_written_bytes_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_bytes_metric('written', device, value, ts)

  @classmethod
  def create_disk_io_time_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_metric('io_time_seconds', device, value, ts)

  @classmethod
  def create_disk_io_time_weighted_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_metric('io_time_weighted_seconds', device, value, ts)

  @classmethod
  def create_disk_io_read_time_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_metric('read_time_seconds', device, value, ts)

  @classmethod
  def create_disk_io_reads_merged_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_metric('reads_merged', device, value, ts)

  @classmethod
  def create_disk_io_writes_merged_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_metric('writes_merged', device, value, ts)

  @classmethod
  def create_disk_io_write_time_metric (cls, device: str, value: str, ts: str):
    return cls.create_disk_metric('write_time_seconds', device, value, ts)

  @classmethod
  def create_disk_io_now_metric (cls, device: str, value: str, ts: str):
    return Metric('node_disk_io_now', value, { 'device': device }, ts)

  @classmethod
  def create_vmstat_metric (cls, title: str, value: str, ts: str):
    return Metric('node_vmstat_%s' % (title,), value, { }, ts)


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
  if title.startswith('cpu_time_'): return MetricsFactory.create_cpu_time_metric(properties['cpu'].strip('cpu'), title.split('_')[-1], value, ts)

  elif title == 'memory_commit_limit': return MetricsFactory.create_memory_commit_limit_metric(value, ts)
  elif title == 'memory_committed_as': return MetricsFactory.create_memory_committed_as_metric(value, ts)

  elif title == 'memory_vmalloc_total': return MetricsFactory.create_memory_vmalloc_total_metric(value, ts)
  elif title == 'memory_vmalloc_chunk': return MetricsFactory.create_memory_vmalloc_chunk_metric(value, ts)
  elif title == 'memory_vmalloc_used': return MetricsFactory.create_memory_vmalloc_used_metric(value, ts)

  elif title == 'memory_huge_pages_total': return MetricsFactory.create_memory_huge_pages_metric(value, ts)
  elif title == 'memory_huge_pages_free': return MetricsFactory.create_memory_huge_pages_free_metric(value, ts)
  elif title == 'memory_huge_page_size': return MetricsFactory.create_memory_huge_pages_size_metric(value, ts)

  elif title == 'memory_swap_free': return MetricsFactory.create_memory_swap_free_metric(value, ts)
  elif title == 'memory_swap_total': return MetricsFactory.create_memory_swap_total_metric(value, ts)

  elif title == 'memory_write_back': return MetricsFactory.create_memory_writeback_metric(value, ts)
  elif title == 'memory_write_back_tmp': return MetricsFactory.create_memory_writeback_tmp_metric(value, ts)

  elif title == 'memory_dirty': return MetricsFactory.create_memory_dirty_metric(value, ts)
  elif title == 'memory_free': return MetricsFactory.create_memory_free_metric(value, ts)
  elif title == 'memory_available': return MetricsFactory.create_memory_available_metric(value, ts)
  elif title == 'memory_inactive': return MetricsFactory.create_memory_inactive_metric(value, ts)
  elif title == 'memory_total': return MetricsFactory.create_memory_total_metric(value, ts)
  elif title == 'memory_mapped': return MetricsFactory.create_memory_mapped_metric(value, ts)
  elif title == 'memory_page_tables': return MetricsFactory.create_memory_page_tables_metric(value, ts)
  elif title == 'memory_cached': return MetricsFactory.create_memory_cached_metric(value, ts)
  elif title == 'memory_slab': return MetricsFactory.create_memory_slab_metric(value, ts)
  elif title == 'memory_sreclaimable': return MetricsFactory.create_memory_reclaimable_metric(value, ts)
  elif title == 'memory_active': return MetricsFactory.create_memory_active_metric(value, ts)

  elif title == 'disk_total': return MetricsFactory.create_filesystem_size_metric(properties['device'], properties['fstype'], properties['path'], value, ts)
  elif title == 'disk_free': return MetricsFactory.create_filesystem_available_metric(properties['device'], properties['fstype'], properties['path'], value, ts)
  
  elif title == 'diskio_write_bytes': return MetricsFactory.create_disk_read_bytes_metric(properties['name'], value, ts)
  elif title == 'diskio_read_bytes': return MetricsFactory.create_disk_written_bytes_metric(properties['name'], value, ts)
  elif title == 'diskio_reads': return MetricsFactory.create_disk_reads_completed_metric(properties['name'], value, ts)
  elif title == 'diskio_writes': return MetricsFactory.create_disk_writes_completed_metric(properties['name'], value, ts)
  elif title == 'diskio_io_time': return MetricsFactory.create_disk_io_time_metric(properties['name'], value, ts)
  elif title == 'diskio_write_time': return MetricsFactory.create_disk_io_write_time_metric(properties['name'], value, ts)
  elif title == 'diskio_read_time': return MetricsFactory.create_disk_io_read_time_metric(properties['name'], value, ts)
  elif title == 'diskio_weighted_io_time': return MetricsFactory.create_disk_io_time_weighted_metric(properties['name'], value, ts)
  elif title == 'diskio_merged_reads': return MetricsFactory.create_disk_io_reads_merged_metric(properties['name'], value, ts)
  elif title == 'diskio_merged_writes': return MetricsFactory.create_disk_io_writes_merged_metric(properties['name'], value, ts)
  elif title == 'diskio_iops_in_progress': return MetricsFactory.create_disk_io_now_metric(properties['name'], value, ts)

  elif title == 'net_bytes_recv': return MetricsFactory.create_network_receive_bytes_metric(value, ts)
  elif title == 'net_bytes_sent': return MetricsFactory.create_network_transmit_bytes_metric(value, ts)

  elif title == 'system_uptime': return [ MetricsFactory.create_up_time_metric(value, ts), MetricsFactory.create_boot_time_metric('0', ts) ]

  elif title == 'system_load5': return MetricsFactory.create_load_metric(5, value, ts)
  elif title == 'system_load15': return MetricsFactory.create_load_metric(15, value, ts)

  return Metric(title, value, properties, ts)

 
translator = Runner(translate)
translator.run()

