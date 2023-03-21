from InfixToPostfix import InfixToPostfix, operators
from AFN import generateAFN, visual_AFN
from AFN_to_AFD import AFD_from_AFN, visual_AFD_from_AFN
from BinaryTree import Node, operators, ArrayInArray, buildTree
from AFN_to_AFD import AFD_from_AFN, state
#exp = '(a|b)*a(a|b)(a|b)'
from direct_AFD import direct_build, visual_directAFD
from mini import Minimization, Minimizacion_Visual


#exp = 'a**(b|c)?*(da+)?a(c|d*)+'

# input de la expresión regular
#exp = input("Ingrese la expresión regular: ")

#exp = 'a(a?b*|c+)b|baa'
#exp = '(b|b)*abb(a|b)*'
#exp = '(a|b)*(a|(bb))*'
#exp = 'ab*ab*'
#exp = 'aab*'
#exp = '(0|ε)((1|ε)|ε)0*'
#exp = '((a|b)*)*ε((a|b)|ε)*'
#exp = 'ab*ab*'
#exp = '(a*|b*)*'
#exp = '(10)*(10)*'
#exp = '(a|b)*a(a|b)(a|b)'

exps = [
    '(a*|b*)c',
    '(b|b)*abb(a|b)*',
    '(a|ε)b(a+)c?',
    '(a|b)*a(a|b)(a|b)',
    'b*ab?',
    'b+abc+',
    'ab*ab*',
    '0(0|1)*0',
    '((ε|0)1*)*',
    '(0|1)*0(0|1)(0|1)',
    '(00)*(11)*',
    '(0|1)1*(0|1)',
    '0?(1|ε)?0*',
    '((1?)*)*',
    '(10)*(10)'
]

exp = exps[0]


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



