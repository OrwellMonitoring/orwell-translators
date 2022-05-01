from tkinter.messagebox import NO
from orwell import Metric, Runner


def translate (dic: dict) -> list:
    metrics_lst=[]
    for key,value in dic.items():
        metrics_lst.append(Metric(key, value[2], dict(), int(value[0])))
    return metrics_lst

translator = Runner(translate)
translator.run()