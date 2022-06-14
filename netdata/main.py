from cmath import pi
import time
from redis import Redis


import requests

from orwell.metric import Metric
from sys import argv, stderr
from os import environ

from orwell.runner import Runner

from orwell.helper import Helper
from orwell.translator import Translator


class PullNetData(Runner):
    #metodos de run
    def consume (self,metrics):
        redis_password = environ.get('REDIS_PASSWORD')
        conn = Redis(password="root")
        conn.rpush("METRICS", metrics)
        conn.close()


    def pull_service(self,host):
        #ver como meter isto a dar de x em x tempo
        url = 'http://10.0.12.81:19999/api/v1/allmetrics?format=prometheus&variables=no&help=no&types=no&timestamps=yes&names=yes&oldunits=yes&hideunits=yes&data=average'
        metrics_lst = self.getMetricsList(url)
        for metric in metrics_lst:
            self.consume(str(metric))



    def run (self):
        #super.run() 
        if argv[1] == "pull":
            args = {}

            redis_password = environ.get('REDIS_PASSWORD')
            

            if redis_password is not None: args['redis_password'] = redis_password
            #aqui fazia o while VER COMO FAZER ISTO DE UMA FORMA MAIS DECENTE
            #while True:
            self.pull_service('10.0.12.81:19999')

                #time.sleep(5) 
                # #como é que vou buscar o argumento de seconds que devo ir buscar???
                #translator deste metrics lst?

    def getMetricsList(self,url):
        resp = requests.get(url=url)
        txt=resp.text.strip().split("\n")
        metrics_lst=[]
        for line in txt:
            linha = line.split(" ")
            ts = linha[-1]
            value = linha[-2]
            properties = linha[:-2]

            if len(properties) > 1:
                
                properties = "_".join(properties)
            else:
                properties=properties[0]
            array = properties.split("{")
            properties = { v[0]:v[1].strip("\"}") for v in [ v.split("=") for v in array[1].split(",") ] } if len(array[1]) > 1 else {}
            title=array[0]
            metrics_lst.append(Metric(title, value, properties, ts))
            
        return metrics_lst


        

if __name__ == '__main__':
    x = PullNetData(any)
    x.run()
