from tkinter.messagebox import NO
from orwell import Metric, Runner


def translate (line: str) -> list:
    if line.startswith("#"): return None
    line = line.split(" ")
    ts=line[-1]
    value=line[-2]
    properties=line[:-2]
    properties="_".join(properties)
    if len(properties) > 1:
            properties = "_".join(properties)
    else:
        properties=properties[0]
    array = properties.split("{")
    if len(array) > 1:
        properties = { v[0]:v[1].strip("\"}") for v in [ v.split("=") for v in array[1].split(",") ] } if len(array[1]) > 1 else {}
    else:
        properties=dict()
    title=array[0]
    return Metric(title, value, properties, ts)

translator = Runner(translate)
translator.run()


