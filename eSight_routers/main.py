from orwell import Metric, Runner
import json
import time
import logging

# we added this flag because we were having an error with Prometheus
# change this flag if you want to keep the original timestamps
change_timestamp = True
def translate (line: str) -> list:
    line = json.loads(line)
    res = []
    logging.info("Received a new message")
    title="esight_slots"
    for key in line.keys():
        interface_name = key
        #Data have all metrics now lets split them
        for x in line[interface_name]["cpu_usage"][0]["resultData"]:
        
            cpu_usage=x
            cpu_name=cpu_usage["neName"]
            cpu_units= cpu_usage["indexUnit"]
            cpu_display_key= cpu_usage["displayValueKey"]
            properties={ "interface_name": interface_name, "units":cpu_units, "cpu_name":cpu_name,"cpu_display_key":cpu_display_key}
            for values in cpu_usage["indexValues"]:
                if change_timestamp:
                    time.sleep(2)
                    res.append(Metric(title+"_cpu_usage", str(values["indexValue"]), properties, str(int(time.time())),"esight_slots"))
                else:
                    res.append(Metric(title+"_send_interface", str(values["indexValue"]), properties, str(values["timestamp"]),"esight_slots"))
        for x in line[interface_name]["mem_usage"][0]["resultData"]:
            mem_usage=x
            mem_name=mem_usage["neName"]
            mem_units= mem_usage["indexUnit"]
            mem_display_key= mem_usage["displayValueKey"]
            properties={ "interface_name": interface_name, "units":mem_units, "cpu_name":mem_name,"cpu_display_key":mem_display_key}
            for values in mem_usage["indexValues"]:
                if change_timestamp:
                    time.sleep(2)
                    res.append(Metric(title+"_mem_usage", str(values["indexValue"]), properties, str(int(time.time())),"esight_slots"))
                else:
                    res.append(Metric(title+"_send_interface", str(values["indexValue"]), properties, str(values["timestamp"]),"esight_slots"))
    return res

logging.basicConfig(format='[%(levelname)s] - %(asctime)s -> %(message)s', level=logging.INFO, datefmt='%d-%m-%Y %H:%M:%S')
translator = Runner(translate)
translator.run()