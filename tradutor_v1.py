from distutils.log import debug
from flask import Flask,make_response
from time import time
app = Flask(__name__)
@app.route('/metrics')
def index():
    dic=dict()
    with open("test.txt", "r") as file:
        lst=[]
        contador=0
        dic=dict()
        for x in file.readlines():
            propetries,metrics,ts=x[2:].split(" ")
            propetries=propetries.split(",")
            title=propetries[0]
            propetries=[p[0]+'="'+p[1]+'"' for p in [prop.split('=') for prop in propetries[1:]]]
            for k, v in [metric.split('=') for metric in metrics.split(',')]:
                dic[title+"_"+k+'{'+','.join(propetries)+'}']=v
        file.close()
    response=make_response(('\n'.join([k+' '+v.replace('i','')+" "+str(int(int(ts)/1000000)) for k, v in dic.items()]) ), 200)
    response.mimetype="text/plain"
    return response
app.run(host="0.0.0.0",debug=True)