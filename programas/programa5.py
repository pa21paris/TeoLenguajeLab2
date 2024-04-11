# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    match = texto
    for i in range(3,0,-1):
        match = re.sub(r'#{'+str(i)+r'}([\w\s]+)\\n', r'<h'+str(i)+r'>\1</h'+str(i)+r'>\\n', match)
    match = re.sub(r'\*{2}(.+)\*{2}', r'<strong>\1</strong>', match)
    match = re.sub(r'\*(.+)\*', r'<em>\1</em>', match)         
    match = re.sub(r'~~(.+)~~', r'<s>\1</s>', match)
    return match

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
