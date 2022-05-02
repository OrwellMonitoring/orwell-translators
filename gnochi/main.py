from orwell import Metric, Runner, MetricsFactory
import sys

def translate (dic: dict) -> list:
    metrics_lst=[]
    dic["memory_free"]=[ dic["memory.usage"][0],dic["memory.usage"][1],
     dic["memory"][2]- dic["memory.usage"][2] ]
    dic.pop("memory.usage")
    for key,value in dic.items():
        data = create_metric(key, value[2], dict(),  str(int(value[0])))
        metrics_lst.append(data)
    return metrics_lst
def create_metric (title: str, value: str, properties: dict, ts: str) -> Metric:
  
  if title == 'memory': return MetricsFactory.create_memory_total_metric(value, ts)
  elif title == 'disk.root.size': return MetricsFactory.create_filesystem_size_metric("", "","", value, ts)
  
 
  elif title == 'compute.instance.booting.time': return [ MetricsFactory.create_up_time_metric(value, ts), MetricsFactory.create_boot_time_metric('0', ts) ]

  elif title== "disk.ephemeral.size": return Metric("ephemeral_size", value, properties, ts)
  return Metric(title, value, properties, ts)

translator = Runner(translate)
translator.run()
