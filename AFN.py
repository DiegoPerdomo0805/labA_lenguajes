# Recibimos un arbol sintactico y lo recorremos para generar los diferentes autómatas finitos no deterministas

import graphviz as gv

operadores = ['*', '|', '.']

def generateAFN(Node):
    if(Node.val in operadores):
        pass
        #cubrimos los casos de los operadores
        #if(Node.val == '*'):
    else:
        # Construimos el automata simple de una letra
        pass