from InfixToPostfix import InfixToPostfix, operators
from AFN import generateAFN, visual_AFN
from AFN_to_AFD import AFD_from_AFN, visual_AFD_from_AFN
from BinaryTree import Node, operators, ArrayInArray, buildTree
from AFN_to_AFD import AFD_from_AFN, state
#exp = '(a|b)*a(a|b)(a|b)'
from direct_AFD import direct_build, visual_directAFD
from mini import Minimization, Minimizacion_Visual


#exp = 'a**(b|c)?*(da+)?a(c|d*)+'
''
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
    '(a*|b*)c',# 0
    '(b|b)*abb(a|b)*',# 1
    '(a|ε)ba+c?',# 2 
    '(a|b)*a(a|b)(a|b)',# 3 - problema con directo
    'b*ab?',# 4 
    'b+abc+',# 5
    'ab*ab*',# 6
    '0(0|1)*0',# 7 
    '((ε|0)1*)*',# 8 
    '(0|1)*0(0|1)(0|1)',# 9 - es la misma expresión que la 3 pero con diferencte alfabeto
    '(00)*(11)*',# 10 
    '(0|1)1*(0|1)',# 11
    '0?(1|ε)?0*',# 12
    '(1?*)*',# 13
    '(10)*(10)'# 14
]

def main(exp):
    #exp = '(ba)?'
    print("Expresión regular: ", exp)
    exp_postfix = InfixToPostfix(exp)

    #exp_postfix = ['32', '9', '|', '10', '|', 'A', 'B', '|', 'C', '|', 'D', '|', 'E', '|', 'F', '|', 'G', '|', 'H', '|', 'I', '|', 'J', '|', 'K', '|', 'L', '|', 'M', '|', 'N', '|', 'O', '|', 'P', '|', 'Q', '|', 'R', '|', 'S', '|', 'T', '|', 'U', '|', 'V', '|', 'W', '|', 'X', '|', 'Y', '|', 'Z', '|', 'a', '|', 'b', '|', 'c', '|', 'd', '|', 'e', '|', 'f', '|', 'g', '|', 'h', '|', 'i', '|', 'j', '|', 'k', '|', 'l', '|', 'm', '|', 'n', '|', 'o', '|', 'p', '|', 'q', '|', 'r', '|', 's', '|', 't', '|', 'u', '|', 'v', '|', 'w', '|', 'x', '|', 'y', '|', 'z', '|', 'A', '.', 'B', '|', 'C', '|', 'D', '|', 'E', '|', 'F', '|', 'G', '|', 'H', '|', 'I', '|', 'J', '|', 'K', '|', 'L', '|', 'M', '|', 'N', '|', 'O', '|', 'P', '|', 'Q', '|', 'R', '|', 'S', '|', 'T', '|', 'U', '|', 'V', '|', 'W', '|', 'X', '|', 'Y', '|', 'Z', '|', 'a', '|', 'b', '|', 'c', '|', 'd', '|', 'e', '|', 'f', '|', 'g', '|', 'h', '|', 'i', '|', 'j', '|', 'k', '|', 'l', '|', 'm', '|', 'n', '|', 'o', '|', 'p', '|', 'q', '|', 'r', '|', 's', '|', 't', '|', 'u', '|', 'v', '|', 'w', '|', 'x', '|', 'y', '|', 'z', '|', '0', '.', '1', '|', '2', '|', '3', '|', '4', '|', '5', '|', '6', '|', '7', '|', '8', '|', '9', '|', '|', '43', '|', '42', '|', '40', '|', '41', '|']

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

    # AFD a partir del AFN
    AFD_de_AFN = AFD_from_AFN(AFN, sigma)

    # Árbol de expresión regular para la construcción directa del AFD
    exp_postfix_2 = exp_postfix
    exp_postfix_2.append( '#')
    exp_postfix_2.append('.')
    exp_postfix_2 = list(exp_postfix_2)
    tree = buildTree(exp_postfix_2.pop(), exp_postfix_2)
    tree.traversePostOrder()
    tree.determineFollowPos()
    arbol = tree.generate_graph()


    #print('Ferrus Manus')
    #tree.post2()
    #print('Rogal Dorn')
    #tree.post3()
    #print('Roboute Guilliman')
    # AFD directo
    AFD_directo = direct_build(tree, sigma, postfix)
    #print('Lion El´Jonson')

    # minimización de AFD a partir del AFN
    AFD_minimizado = Minimization(AFD_de_AFN, sigma)
    #print('Leman Russ')

    # minimización de AFD directo
    AFD_directo_minimizado = Minimization(AFD_directo, sigma)
    #print('Jaghatai Khan')

    """
    print('\n')
    print('AFD a partir del AFN')
    print(AFD_de_AFN)
    print('\n')
    print('AFD directo')
    print(AFD_directo)
    print('\n')"""
    """print('AFD a partir del AFN minimizado')
    print(AFD_minimizado)
    print('\n')
    print('AFD directo minimizado')
    print(AFD_directo_minimizado)
    """

    Minimizacion_Visual(AFD_directo_minimizado, 'direct_AFD_minimizado', exp)
    Minimizacion_Visual(AFD_minimizado, 'AFD a partir del AFN minimizado', exp)
    visual_directAFD(AFD_directo, exp)
    visual_AFD_from_AFN(AFD_de_AFN, exp)
    visual_AFN(AFN, exp)
    arbol.attr(label=exp)
    arbol.render('arbol', view=True, directory='./visual_results/', cleanup=True, format='png')


import time

for exp in exps:
    print('-'*50)
    main(exp)
    print('-'*50)
    time.sleep(20)

#main(exps[0])