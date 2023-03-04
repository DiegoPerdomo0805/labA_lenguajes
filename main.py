from InfixToPostfix import InfixToPostfix, operators
from AFN import generateAFN, visual_AFN

#exp = '(a|b)*a(a|b)(a|b)'

exp = 'a**(b|c)?*(da+)?a(c|d*)+'

# input de la expresión regular
#exp = input("Ingrese la expresión regular: ")

exp = 'a(a?b*|c+)b|baa'
exp = 'aab*'
exp = '(0|ε)((1|ε)|ε)0*'


exp_postfix = InfixToPostfix(exp)

if exp_postfix == False:
    print("Expresión regular inválida")
    exit()

sigma = []
for e in exp_postfix:
    if e not in operators and e not in sigma and e != 'ε':
        sigma.append(e)

print("Alfabeto: ", sigma)


postfix = ''.join(exp_postfix)
print("Expresión regular formato postfix: ", postfix)
AFN = generateAFN(exp_postfix)  
#visual_AFN(AFN)
"""
print("AFN: ", AFN.start.name)
for e in AFN.start.transitions:
    print(e.symbol, e.to.name)"""

# recorrido epsilon

inicio = AFN.start
print("Recorrido epsilon: ", inicio.name)

estados = []

estado_inicial = []

# a la hora de crear un nuevo estado, es necesario tener en mente que la transición no se puede repetir dos veces seguidas
# a menos que sea una transición epsilon
# un ejemplo de esto sería aab*, donde el estado inicial es el estado 0, y el estado final es el estado 3
# el afn sería el siguiente:
# 0 -> 1 con a
# 1 -> 2 con a
# 2 -> 3 con b
# 3 -> 3 con b
# 3 -> 4 con ε


for e in inicio.transitions:
    print(e.symbol, e.to.name)
print(' final ', AFN.end.name)

"""
def estado_nuevo(inicio, transicion, estado):
    for e in inicio.transitions:
        if e.symbol in transicion and e.to not in estado:
            #print(e.to.name)
            #print(" de ", inicio.name, " a ", e.to.name, " con ", e.symbol)
            estado.append(e.to)
            estado_nuevo(e.to, transicion, estado)"""

#estado_nuevo(inicio, ['ε', 'a'], estado_inicial)
"""
for e in estado_inicial:
    print("Recorrido epsilon: ", e.name)"""

class state:
    def __init__(self, name, contains):
        self.name = name
        self.contains = contains
        self.transitions = {}
        self.isAccept = False

    def isAccept(self, end):
        if end in self.contains:
            self.isAccept = True

    def addTransition(self, symbol, to):
        self.transitions[symbol] = to
        
        


def recorrido_epsilon(inicio, lista):
    for e in inicio.transitions:
        if e.symbol == 'ε' and e.to not in lista:
            #print("Recorrido epsilon: ", e.to.name)
            lista.append(e.to)
            recorrido_epsilon(e.to, lista)

def new_state(symbol, lista):
    temp = []
    for e in lista:
        if e.checkTransition(symbol) != None:
            temp_state = e.checkTransition(symbol)
            recorrido_epsilon(temp_state, temp)

    return temp

estado_inicial.append(inicio)
recorrido_epsilon(inicio, estado_inicial)
print("Recorrido epsilon: ", estado_inicial)
for e in estado_inicial:
    print(e.name)


"""
while flag:
    flag = False
    for e in inicio.transitions:
        if e.symbol == 'ε':
            #print(e.to.name)
            print(" de ", inicio.name, " a ", e.to.name, " con ", e.symbol)
            inicio = e.to
            flag = True"""




# recorrido de transiciones con símbolos de manera recursiva


# recorrido 