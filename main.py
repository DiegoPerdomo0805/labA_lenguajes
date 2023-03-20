from InfixToPostfix import InfixToPostfix, operators
from AFN import generateAFN, visual_AFN
from AFN_to_AFD import AFD_from_AFN, visual_AFD_from_AFN
from BinaryTree import Node, operators, ArrayInArray, buildTree
from AFN_to_AFD import AFD_from_AFN, state
#exp = '(a|b)*a(a|b)(a|b)'
from direct_AFD import direct_build, visual_directAFD
from mini import Minimization, Minimizacion_Visual


exp = 'a**(b|c)?*(da+)?a(c|d*)+'

# input de la expresión regular
#exp = input("Ingrese la expresión regular: ")

#exp = 'a(a?b*|c+)b|baa'
#exp = '(b|b)*abb(a|b)*'
#exp = '(a|b)*(a|(bb))*'
#exp = 'ab*ab*'
#exp = 'aab*'
exp = '(0|ε)((1|ε)|ε)0*'
exp = '((a|b)*)*ε((a|b)|ε)*'
#exp = 'ab*ab*'
#exp = '(a*|b*)*'
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



# minimización de AFD a partir del AFN
AFD_minimizado = Minimization(AFD_de_AFN, sigma)

# minimización de AFD directo
AFD_directo_minimizado = Minimization(AFD_directo, sigma)




# apartado visual
visual_AFN(AFN)

visual_AFD_from_AFN(AFD_de_AFN)

visual_directAFD(AFD_directo)

Minimizacion_Visual(AFD_minimizado, 'AFD a partir del AFN minimizado')

Minimizacion_Visual(AFD_directo_minimizado, 'AFD directo minimizado')



# experimentos minimización

"""





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


#print(' - ',getTransitions(groups[0], groups, sigma))


# subdivide los grupos en subgrupos si es que no son atómicos

def isAtomic(grupo, grupos, sigma):
    if len(grupo) == 1:
        return True
    else:
        #transitions = []
        transitions = getTransitions(grupo, grupos, sigma)
        #print(transitions)

        first = transitions[grupo[0].name]
        #print(first)
        for i in range(1, len(grupo)):
            temp = transitions[grupo[i].name]
            #print(temp)
            #print(temp == first)
            if temp  != first:  
                return False
        return True

        
    
def Divide(group, grupos, sigma):
    subgroups = [group]
    #print('subgroups', subgroups)
    i = 0
    while i < len(subgroups):
        subgroup = subgroups[i]
        if not isAtomic(subgroup, grupos, sigma):
            transitions = getTransitions(subgroup, grupos, sigma)
            #print(transitions.values())
            for target_group in transitions.values():
                new_subgroup = [s for s in subgroup if transitions[s.name] == target_group]
                if new_subgroup not in subgroups:
                    subgroups.append(new_subgroup)
            subgroups.remove(subgroup)
            i -= 1
        i += 1
    for e in subgroups:
        if not isAtomic(e, grupos, sigma):
            #print('entré 159')
            Divide(e, grupos, sigma)
    #return subgroups
    #print('subgroups')
    grupos.remove(group)
    grupos.extend(subgroups)

"""

# separar estados de aceptación y no aceptación
#print(AFD_de_AFN)
"""groups = []
accept = []
not_accept = []


for e in AFD_de_AFN:

    if e.isAccept:
        accept.append(e)
    else:
        not_accept.append(e)




groups.append(accept)
if not_accept != []:
    groups.append(not_accept)



#print(groups)






    flag = True
    while flag:
        for e in groups:
            #print(isAtomic(e, groups, sigma),'\n')
            if isAtomic(e, groups, sigma):
                #print(e, 'es atómico')
                flag = False
            else:
                #print(e, 'no es atómico')
                Divide(e, groups, sigma)
                flag = True
                #print(groups)
                #print('\n')

    #print(groups)

    # crear estados usando state class

    from AFN_to_AFD import state


    new_states = []
    i = 0
    for e in groups:
        new_states.append(state( f"q{i}", e))
        i += 1

    for e in new_states:
        #print(e.name)
        for s in sigma:
            transition = e.contains[0].transitions[s]
            if transition != None:
                for e2 in new_states:
                    if transition in e2.contains:
                        e.addTransition(s, e2)

            else:
                e.addTransition(s, None)




for e in new_states:
    print(e.name)
    for t in e.transitions:
        print(t, e.transitions[t].name)
"""

#for e in new_states:
    