# -*- coding: utf-8 -*-

def handler(event, context):

    nombre = event.get('nombre')
    edad = event.get('edad')

    return "Tu nombre es {} y tienes {}".format(nombre, str(edad))
