# -*- coding: utf-8 -*-
import requests as req

def handler(event, context):
    # Your code goes here!

    nombre = event.get('nombre')
    edad = event.get('edad')

    return "Tu nombre es {} y tienes {}".format(nombre, str(edad))
