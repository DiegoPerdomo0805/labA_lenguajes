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
visual_AFN(AFN)

AFD_de_AFN = AFD_from_AFN(AFN, sigma)
visual_AFD_from_AFN(AFD_de_AFN)


exp_postfix_2 = exp_postfix
exp_postfix_2.append( '#')
exp_postfix_2.append('.')

exp_postfix_2 = list(exp_postfix_2)
tree = buildTree(exp_postfix_2.pop(), exp_postfix_2)
tree.traversePostOrder()
tree.determineFollowPos()
#print()
#tree.post2()

print()
#tree.post3()


#print('Valor del elemento final de la regex: ',tree.searchPos(len(postfix)).val)  
#print('\n\n\n')


AFD_directo = direct_build(tree, sigma, postfix)
visual_directAFD(AFD_directo)

"""for e in AFD_directo:
    print( e.name, ' - ' , e.contains, ' - ' , e.isAccept)
          
    for f in e.transitions:
        print(' - ', e.name, '->', f, '->', e.transitions[f].name)
"""
#print(len(postfix), postfix, postfix[len(postfix)-1], tree.searchPos(len(postfix)+1).val)



"""Dtran = []
Dstates = []
Dstates.append(tree.first_pos)
Marked = []

# mientras exista un estado no marcado, se procede a marcarlo
#while Marked != Dstates:
#    e = next(s for s in Dstates if s not in Marked)
for e in Dstates:
    if e not in Marked:
        Marked.append(e)
        # se obtiene el conjunto de estados alcanzables
        # con cada uno de los símbolos del regex
        #i = 0
        #while i < len(postfix):
        for i in range(len(postfix)):
            acu = []
            if postfix[i] in sigma:
                if (i+1) in e:
                    #print(i+1, e)
                    #print(tree.searchPos(i+1).val)
                    #print(tree.searchPos(i+1).follow_pos)
                    #acu.append(tree.searchPos(i+1).follow_pos)
                    temp_awedowed = tree.searchPos(i+1).follow_pos
                    for e2 in temp_awedowed:
                        if e2 not in acu:
                            acu.append(e2)
                    print(acu)

                    # comprobar que no existas dos transiciones con el mismo símbolo
                    # en el mismo estado
                    # si existe, se concatena el conjunto de estados alcanzables
                    # de la transición existente con el nuevo conjunto de estados
                    # alcanzables
                    for t in Dtran:
                        if t[0] == e and t[1] == postfix[i]:
                            #t[2] = t[2] + acu
                            for e2 in acu:
                                if e2 not in t[2]:
                                    t[2].append(e2)
                            acu = t[2]
                    


                    # se determina si el nuevo conjunto de estados alcanzables
                    # ya existe en Dstates, si no existe, se agrega a Dstates
                    #if acu not in Dstates:
                    for j in Dstates:
                        if not ArrayInArray(acu, j):
                            #acu = j
                            Dstates.append(acu)
                    # se crea la transición
                    if ArrayInArray(acu, e):
                        #temp = [e, e, postfix[i]]
                        temp = [e, postfix[i], e]
                    else:
                        #temp = [e, acu, postfix[i]]
                        temp = [e, postfix[i], acu]
                    if temp not in Dtran:
                        Dtran.append(temp)
        #i += 1
    
#print(Dtran)
print('Estados: ',Dstates)
print('Marked',Marked)
for e in Dtran:
    print(' *- ',e)


direct_states = []
i = 0
for e in Marked:
    direct_states.append(state(f"S{i}",e))
    i += 1


for e in Dtran:
    for e2 in direct_states:
        if e[0] == e2.contains:
            for e3 in direct_states:
                if e[2] == e3.contains:
                    e2.addTransition(e[1], e3)

#for e in direct_states:
#    print(e.name, e.contains)
for e in direct_states:
    print(e.name, e.contains)
    for f in e.transitions:
        print('  *- ', e.name, '->' ,f, '->' , e.transitions[f].name)"""