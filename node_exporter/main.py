#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Authors: Alexandre Serras (alexandreserras@ua.pt), Gonçalo Leal (goncalolealsilva@ua.pt)
# Date: 02-05-2022

# Description:
# Prometheus' metrics reader and sender to redis

from orwell import Metric, Runner
import json

def translate (line: str) -> list:
    line = json.loads(line)
    res = []
    for l in line:

        if l.startswith("#"): continue

        l = l.split(" ")
        ts=l[-1]
        value=l[-2]
        title, properties=l[0].split("{")
        # properties="_".join(properties)
        # if len(properties) > 1:
        #        properties = "_".join(properties)
        # else:
        # properties=properties[0]
        # array = properties.split(",")

        properties = { v[0]:v[1].strip("\"}") for v in [ v.split("=") for v in properties.split(",") ] }
        print(properties)
        # title=array[0]
        res.append(Metric(title, value, properties, ts, properties["instance"]))
    return res

translator = Runner(translate)
translator.run()

