from InfixToPostfix import InfixToPostfix, operators
from AFN import generateAFN, visual_AFN
from AFN_to_AFD import AFD_from_AFN, visual_AFD_from_AFN
from BinaryTree import Node, operators, ArrayInArray, buildTree
from AFN_to_AFD import AFD_from_AFN, state
#exp = '(a|b)*a(a|b)(a|b)'
from direct_AFD import direct_build, visual_directAFD

exp = 'a**(b|c)?*(da+)?a(c|d*)+'

# input de la expresión regular
#exp = input("Ingrese la expresión regular: ")

#exp = 'a(a?b*|c+)b|baa'
#exp = '(b|b)*abb(a|b)*'
#exp = '(a|b)*(a|(bb))*'
#exp = 'ab*ab*'
#exp = 'aab*'
#exp = '(0|ε)((1|ε)|ε)0*'
exp = 'ab*ab*'
#exp = '(10)*(10)*'
#exp = '(a|b)*a(a|b)(a|b)'


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

print('\n')

# AFD a partir del AFN
AFD_de_AFN = AFD_from_AFN(AFN, sigma)

print('\n')
# Árbol de expresión regular para la construcción directa del AFD
exp_postfix_2 = exp_postfix
exp_postfix_2.append( '#')
exp_postfix_2.append('.')
exp_postfix_2 = list(exp_postfix_2)
tree = buildTree(exp_postfix_2.pop(), exp_postfix_2)
tree.traversePostOrder()
tree.determineFollowPos()

# AFD directo
AFD_directo = direct_build(tree, sigma, postfix)





# apartado visual
#visual_AFN(AFN)
#visual_AFD_from_AFN(AFD_de_AFN)
#visual_directAFD(AFD_directo)


# experimentos minimización
print('\n')



# separar estados de aceptación y no aceptación
#print(AFD_de_AFN)
groups = []
accept = []
not_accept = []


for e in AFD_de_AFN:

    if e.isAccept:
        accept.append(e)
    else:
        not_accept.append(e)


groups.append(accept)
groups.append(not_accept)

#print(groups)


def getTransitions(group, groups , sigma):
    transitions = {}
    for e in group:
        transitions[e.name] = {}
        for s in sigma:
            if e.checkTransition(s) != None:
                indice = -1
                for f in groups:
                    if e.checkTransition(s) in f:
                        indice = groups.index(f)
                #transitions.append([e.name, s,  indice])
                #transitions[e.name, s] = indice
                transitions[e.name][s] = indice
            else:
                #transitions.append([e.name, s,  None])
                #transitions[e.name, s] = None
                transitions[e.name][s] = None
    return transitions





# subdivide los grupos en subgrupos si es que no son atómicos

def isAtomic(grupo, grupos, sigma):
    if len(grupo) == 1:
        return True
    else:
        #transitions = []
        transitions = getTransitions(grupo, grupos, sigma)
        print(transitions)

        first = transitions[grupo[0].name]
        #print(first)
        for i in range(1, len(grupo)):
            temp = transitions[grupo[i].name]
            #print(temp)
            #print(temp == first)
            if temp  != first:  
                return False
        return True

        
    
#def Divide(group, groups, sigma):
    



for e in groups:
    print(isAtomic(e, groups, sigma),'\n')

 


