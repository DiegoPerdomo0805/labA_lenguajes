import graphviz
# Description: This program converts an AFN to an AFD

# clase para los estados del AFD generados a partir del AFN
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

    def checkTransition(self, symbol):
        if symbol in self.transitions:
            return self.transitions[symbol]
        else:
            return None



# Función para recorrer el AFN a partir de un estado inicial
# y obtener todos los estados a los que se puede llegar con un
# recorrido epsilon
def recorrido_epsilon(inicio, lista):
    for e in inicio.transitions:
        if e.symbol == 'ε' and e.to not in lista:
            #print("Recorrido epsilon: ", e.to.name)
            lista.append(e.to)
            recorrido_epsilon(e.to, lista)



# Función para obtener los estados a los que se puede llegar
# desde un estado con un símbolo dado
def new_state(symbol, lista):
    temp = []
    for e in lista:
        if e.checkTransition(symbol) != None:
            temp_state = e.checkTransition(symbol)
            temp.append(temp_state)
            recorrido_epsilon(temp_state, temp)

    return temp

def AFD_from_AFN(AFN, sigma):
    beginning = AFN.start
    end = AFN.end

    states = []

    estado_inicial = []
    estado_inicial.append(beginning)
    recorrido_epsilon(beginning, estado_inicial)

    if end in estado_inicial:
        begin_state = state('S0', estado_inicial)
        begin_state.isAccept = True
    else:
        begin_state = state('S0', estado_inicial)
    
    states.append(begin_state)

    estados_content = []
    estados_content.append(begin_state.contains)

    i = 1

    for e in states:
        for symbol in sigma:
            new = new_state(symbol, e.contains)

            # si el nuevo estado no está en la lista de estados y no

            if new not in estados_content and new != []:


                #estados.append(new)
                n_state = state(f"S{i}", new)
                if end in new:
                    n_state.isAccept = True
                e.addTransition(symbol, n_state)
                states.append(n_state)
                estados_content.append(new)
            else:
                if new != []: # si el estado no es vacío, quiere dec
                    for i in range(len(estados_content)):
                        if estados_content[i] == new:
                            e.addTransition(symbol, states[i])
                            """break
                    e.addTransition(symbol, None)"""
                else:
                    e.addTransition(symbol, None)
            i += 1
                #e.addTransition(symbol, new)

    return states

def visual_AFD_from_AFN(AFN):
    g = graphviz.Digraph(comment='AFD_from_AFN', format='png')
    g.attr('node', shape='circle')
    g.attr('node', style='filled')
    g.attr('node', color='lightblue2')
    g.attr('node', fontcolor='black')
    g.attr('edge', color='black')
    g.attr('edge', fontcolor='black')
    g.attr('edge', fontsize='20')
    g.attr('graph', rankdir='LR')
    g.attr('graph', size='17')


    for e in AFN:
        if e.isAccept:
            g.node(e.name, e.name, shape='doublecircle')
        else:
            g.node(e.name, e.name)
        for k, v in e.transitions.items():
            if v != None:
                g.edge(e.name, v.name, label=k)
    g.render('AFD_from_AFN', view=True, directory='./visual_results/') 

    