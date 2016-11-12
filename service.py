# -*- coding: utf-8 -*-
import json

def handler(event, context):

    nombre = event.get('nombre')
    edad = event.get('edad')

    return json.dumps({"received":True})
