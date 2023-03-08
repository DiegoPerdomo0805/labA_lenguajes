from InfixToPostfix import InfixToPostfix, operators
from AFN import generateAFN, visual_AFN

#exp = '(a|b)*a(a|b)(a|b)'

exp = 'a**(b|c)?*(da+)?a(c|d*)+'

# input de la expresión regular
#exp = input("Ingrese la expresión regular: ")

exp = 'a(a?b*|c+)b|baa'
exp = 'aab*'
exp = '(0|ε)((1|ε)|ε)0*'
exp = 'ab*ab*'


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
fin = AFN.end
#print("Recorrido epsilon: ", inicio.name)

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


#### for e in inicio.transitions:
####     print(e.symbol, e.to.name)
#### print(' final ', AFN.end.name)

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
            temp.append(temp_state)
            recorrido_epsilon(temp_state, temp)

    return temp

estado_inicial.append(inicio)
recorrido_epsilon(inicio, estado_inicial)

if fin in estado_inicial:
    begin_state = state('S0', estado_inicial)
    begin_state.isAccept = True
else:
    begin_state = state('S0', estado_inicial)



print("estado inicial: ", begin_state.name, "\ntransiciones: ", begin_state.transitions, "\naceptación: ", begin_state.isAccept)
for e in begin_state.contains:
    print(e.name)

estados.append(begin_state)

estados_content = []

estados_content.append(begin_state.contains)


i = 1
for e in estados:
    for symbol in sigma:
        new = new_state(symbol, e.contains)

        # si el nuevo estado no está en la lista de estados y no es vacío

        if new not in estados_content and new != []:


            #estados.append(new)
            n_state = state(f"S{i}", new)
            if fin in new:
                n_state.isAccept = True
            e.addTransition(symbol, n_state)
            estados.append(n_state)
            estados_content.append(new)
        else:
            if new != []: # si el estado no es vacío, quiere decir que es una transición a un estado ya existente
                for i in range(len(estados_content)):
                    if estados_content[i] == new:
                        e.addTransition(symbol, estados[i])
                        """break
                e.addTransition(symbol, None)"""
            else:
                e.addTransition(symbol, None)
        i += 1
            #e.addTransition(symbol, new)



print('------------------------------------------------------------')

for e in estados:
    print("estado: ", e.name, ', ', e, "\naceptación: ", e.isAccept)
    temp = ''
    for i in e.contains:
        #print(i.name, type(i.name))
        temp += f"{i.name}" + ', '
    print("contiene: ", temp)
    for k, v in e.transitions.items():
        if v != None:
            print(k, v.name)
        else:
            print(k, v)
    print('------------------------------------------------------------')

#estad0_2 = new_state('0', estado_inicial)




# recorrido de transiciones con símbolos de manera recursiva


# recorrido 