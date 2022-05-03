from orwell import Metric, Runner, MetricsFactory
import json

import sys

def translate (dic: dict) -> list:
    dic = json.loads(dic)
    metrics_lst=[]

    if 'vcpus' in dic.keys():
      for cpu in range(int(dic['vcpus'][2])):
        metrics_lst.append(MetricsFactory.create_cpu_time_metric(cpu, "", "0", dic['vcpus'][0], dic['instance']))

    if 'memory' in dic.keys():
      metrics_lst.append(MetricsFactory.create_memory_total_metric(str(dic['memory'][2]), dic['memory'][0], dic['instance']))
    
    if "memory.usage" in dic.keys():
      dic["memory_free"]=[ dic["memory.usage"][0],dic["memory.usage"][1],
      dic["memory"][2]- dic["memory.usage"][2] ]
      metrics_lst.append(MetricsFactory.create_memory_available_metric(dic["memory_free"][2],dic["memory_free"][0],dic['instance']))
    
    if "disk.root.size" in dic.keys():
      tmp=int(dic["disk.root.size"][2])*1024**3
      metrics_lst.append(MetricsFactory.create_filesystem_size_metric("","","/",str(tmp),dic["disk.root.size"][0],dic['instance']))
    return metrics_lst


translator = Runner(translate)
translator.run()