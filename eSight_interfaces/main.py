from orwell import Metric, Runner
import json
import time
import logging

# we added this flag because we were having an error with Prometheus
# change this flag if you want to keep the original timestamps
change_timestamp = True

def translate (line: str) -> list:
    line = json.loads(line)
    logging.info("Received a new message")

    res = []
    title="esight_interface"
    for key in line.keys():
        interface_name = key

        if "sending_rate" in line[interface_name].keys() \
            and "resultData" in line[interface_name]["sending_rate"].keys() \
            and len(line[interface_name]["sending_rate"]["resultData"]) > 0:

            logging.info(f"Translating sending rate metrics for {interface_name}")

            send_data = line[interface_name]["sending_rate"]["resultData"][0]

            send_interface_user_friendly_name = send_data["neName"]
            send_index_units = send_data["indexUnit"]

            properties = {"interface_name": interface_name, "units": "Kbps", "interface_user_friendly_name": send_interface_user_friendly_name}
            for values in send_data["indexValues"]:

                if send_index_units == "Mbps":
                    # convert value from Mbps to Kbps
                    values["indexValue"] = float(values["indexValue"]) * 1000

                if change_timestamp:
                    time.sleep(2)
                    res.append(Metric(title+"_send_interface", str(values["indexValue"]), properties, str(int(time.time())), "esight_if"))
                    logging.info(str(res[-1]))
                else:
                    res.append(Metric(title+"_send_interface", str(values["indexValue"]), properties, str(values["timestamp"]), "esight_if"))
        else:
            logging.info(f"{interface_name} has sent a mesage with no sending rate metrics")
        
        if "receiving_rate" in line[interface_name].keys() \
            and "resultData" in line[interface_name]["receiving_rate"].keys() \
            and len(line[interface_name]["receiving_rate"]["resultData"]) > 0:

            logging.info(f"Translating receiving rate metrics for {interface_name}")

            receive_data = line[interface_name]["receiving_rate"]["resultData"][0]

            receive_interface_user_friendly_name = receive_data["neName"]
            receive_index_units = receive_data["indexUnit"]

            properties={"interface_name": interface_name, "units": "Kbps", "interface_user_friendly_name": receive_interface_user_friendly_name}
            for values in receive_data["indexValues"]:
                if receive_index_units == "Mbps":
                    # convert value from Mbps to Kbps
                    values["indexValue"]=float(values["indexValue"]) * 1000

                if change_timestamp:
                    time.sleep(2)
                    res.append(Metric(title+"_receive_interface", str(values["indexValue"]), properties, str(int(time.time())),"esight_if"))
                else:
                    res.append(Metric(title+"_receive_interface", str(values["indexValue"]), properties, str(values["timestamp"]),"esight_if"))
        else:
            logging.info(f"{interface_name} has sent a mesage with no receiving rate metrics")


    logging.info(f"Sending Metrics from {interface_name}")
    logging.info(res)
    return res

logging.basicConfig(format='[%(levelname)s] - %(asctime)s -> %(message)s', level=logging.INFO, datefmt='%d-%m-%Y %H:%M:%S')

translator = Runner(translate)
translator.run()
