from orwell import Metric, Runner
import json
import time
import logging
def translate (line: str) -> list:
    line = json.loads(line)
    res = []
    logging.info(line)
    title="esight_interface"
    for key in line.keys():
        interface_name = key
        #Data have all metrics now lets split them
        try:
            send_data=line[interface_name]["sending_rate"]["resultData"][0]
            send_interface_user_friendly_name=send_data["neName"]
            send_index_units= send_data["indexUnit"]
            properties={ "interface_name": interface_name, "units":send_index_units, "interface_user_friendly_name":send_interface_user_friendly_name}
            for values in send_data["indexValues"]:
                if send_index_units == "Mbps":
                    send_index_units="Kbps" 
                    values["indexValue"]=values["indexValue"]*1000
                res.append(Metric(title+"_send_interface", str(values["indexValue"]), properties, str(int(time.time())),"perf"))
            receive_data=line[interface_name]["receiving_rate"]["resultData"][0]
            receive_interface_user_friendly_name=receive_data["neName"]
            receive_index_units= receive_data["indexUnit"]
            properties={"interface_name": interface_name, "units":receive_index_units, "interface_user_friendly_name":receive_interface_user_friendly_name}
            for values in receive_data["indexValues"]:
                if receive_index_units == "Mbps":
                    receive_index_units="Kbps" 
                    values["indexValue"]=values["indexValue"]*1000
                res.append(Metric(title+"_receive_interface", str(values["indexValue"]), properties, str(int(time.time())),"perf"))
        except:
            logging.info("ERRO AO CRIAR MÉTRICAS")
            continue
    return res
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
translator = Runner(translate)
translator.run()
