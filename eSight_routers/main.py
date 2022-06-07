from orwell import Metric, Runner
import json
import time
def translate (line: str) -> list:
    line = json.loads(line)
    res = []
    print(line)
    title="esight_slots"
    for key in line.keys():
        interface_name = key
        #Data have all metrics now lets split them
        try:
            for x in line[interface_name]["cpu_usage"]["resultData"]:
            
                cpu_usage=x
                cpu_name=cpu_usage["indexName"]
                cpu_units= cpu_usage["indexUnit"]
                cpu_display_key= cpu_usage["displayValueKey"]
                properties={ "interface_name": interface_name, "units":cpu_units, "cpu_name":cpu_name,"cpu_display_key":cpu_display_key}
                for values in cpu_usage["indexValues"]:
                    res.append(Metric(title+"_cpu_usage", str(values["indexValue"]), properties, str(int(time.time())),"perf"))
                    #res.append(Metric(title+"_send_interface", str(values["indexValue"]), properties, str(values["timestamp"]),"perf"))
            for x in line[interface_name]["mem_usage"]["resultData"]:
                mem_usage=x
                mem_name=mem_usage["indexName"]
                mem_units= mem_usage["indexUnit"]
                mem_display_key= mem_usage["displayValueKey"]
                properties={ "interface_name": interface_name, "units":mem_units, "cpu_name":mem_name,"cpu_display_key":mem_display_key}
                for values in mem_usage["indexValues"]:
                    res.append(Metric(title+"_mem_usage", str(values["indexValue"]), properties, str(int(time.time())),"perf"))
                    #res.append(Metric(title+"_send_interface", str(values["indexValue"]), properties, str(values["timestamp"]),"perf"))
        except:
            print("NO DATA")
            continue
    return res

translator = Runner(translate)
translator.run()