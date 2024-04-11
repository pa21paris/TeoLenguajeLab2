# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    match = re.findall(r'"timestamp": "T (.+):(.+):(.+) (..:..):..",', texto)
    months=['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
    ret = map(lambda time : time[2]+" de "+months[int(time[1])-1]+" del "+time[0]+" a las "+time[3]+" hs.", match)
    ret = '\n'.join(ret)
    return ret

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
