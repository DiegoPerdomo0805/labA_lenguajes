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
    '(a*|b*)c',
    '(b|b)*abb(a|b)*',
    '(a|ε)ba+c?',
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
    '(1?*)*',
    '(10)*(10)'
]

# pruebas
strings = [
    # '(a*|b*)c'
    ["aac", "bbbc", "c", "ac"],
    # '(b|b)*abb(a|b)*'
    ["abb", "babbaa", "abb", "bbabb"],
    # '(a|ε)ba+c?'
    ["ba", "abaac", "ba", "baa"],
    # '(a|b)*a(a|b)(a|b)'
    ["aabab", "baaab", "aa", "abaa"],
    # 'b*ab?'
    ["aa", "bbb", "b", "ab"],
    # 'b+abc+'
    ["bc", "bbbc", "babc", "babc"],
    # 'ab*ab*'
    ["aba", "abbbb", "abab", "ab"],
    # '0(0|1)*0'
    ["0101", "001", "00", "010"],
    # '((ε|0)1*)*'
    ["11", "100", "", "01010"],
    # '(0|1)*0(0|1)(0|1)'
    ["1010", "001", "010", "0100"],
    # '(00)*(11)*'
    ["001100", "000111", "", "0011"],
    # '(0|1)1*(0|1)'
    ["111", "01010", "101", "1111"],
    # '0?(1|ε)?0*'
    ["100100", "101", "000", "010"],
    # '(1?*)*'
    ["111", "01010", "", "1"],
    # '(10)*(10)'
    ["1010", "10101", "10", "1010"]
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

    return AFN, AFD_de_AFN, AFD_directo, AFD_minimizado, AFD_directo_minimizado, arbol, exp

    

def visualRepresentation(AFN, AFD_de_AFN, AFD_directo, AFD_minimizado, AFD_directo_minimizado, arbol, exp):
    Minimizacion_Visual(AFD_directo_minimizado, 'direct_AFD_minimizado', exp)
    Minimizacion_Visual(AFD_minimizado, 'AFD a partir del AFN minimizado', exp)
    visual_directAFD(AFD_directo, exp)
    visual_AFD_from_AFN(AFD_de_AFN, exp)
    visual_AFN(AFN, exp)
    arbol.attr(label=exp)
    arbol.render('arbol', view=True, directory='./visual_results/', cleanup=True, format='png')


def writeLog(bitacora, nombre):
    with open(nombre, 'w', encoding='utf-8') as f:
        f.write(bitacora)



import time
from AFN_to_AFD import simulation, minimizedSimulation
#for exp in exps:
#    AFN, AFD_de_AFN, AFD_directo, AFD_minimizado, AFD_directo_minimizado, arbol, exp = main(exp)
#    visualRepresentation(AFN, AFD_de_AFN, AFD_directo, AFD_minimizado, AFD_directo_minimizado, arbol, exp)


print(' # '*50)
bitacora = ""
for reg in range(0, len(exps)):
    AFN, AFD_de_AFN, AFD_directo, AFD_minimizado, AFD_directo_minimizado, arbol, exp = main(exps[reg])
    visualRepresentation(AFN, AFD_de_AFN, AFD_directo, AFD_minimizado, AFD_directo_minimizado, arbol, exp)
    bitacora += "Expresión regular: " + exp + "\n\n"
    for test in strings[reg]:
        print('Cadena de prueba: ' + test + '\n')
        bitacora += "Cadena de prueba: " + test + "\n"
        AFD_Result, Tbitacora = simulation(AFD_de_AFN[0], test)
        bitacora += "AFD a partir del AFN" + "\n"
        bitacora += Tbitacora
        bitacora += " - Cadena aceptada" if AFD_Result else " - Cadena no aceptada"
        bitacora += "\n\n"
        print(' AFN a AFD: ' + str(AFD_Result))

        AFD_Result, Tbitacora = simulation(AFD_directo[0], test)
        bitacora += "AFD directo" + "\n"
        bitacora += Tbitacora
        bitacora += " - Cadena aceptada" if AFD_Result else " - Cadena no aceptada"
        bitacora += "\n\n"
        print(' AFD directo: ' + str(AFD_Result))

        AFD_Result, Tbitacora = minimizedSimulation(AFD_minimizado, test)
        bitacora += "AFD a partir del AFN minimizado" + "\n"
        bitacora += Tbitacora
        bitacora += " - Cadena aceptada" if AFD_Result else " - Cadena no aceptada"
        bitacora += "\n\n"
        print(' AFD a partir del AFN minimizado: ' + str(AFD_Result))

        AFD_Result, Tbitacora = minimizedSimulation(AFD_directo_minimizado, test)
        bitacora += "AFD directo minimizado" + "\n"
        bitacora += Tbitacora
        bitacora += " - Cadena aceptada" if AFD_Result else " - Cadena no aceptada"
        bitacora += "\n\n"
        print(' AFD directo minimizado: ' + str(AFD_Result))

        print(' - ' * 50)
        time.sleep(1)
    bitacora += " - " * 50 + "\n\n"
    print(' # '*50)
    time.sleep(10)
    #time.sleep(30)

writeLog(bitacora, 'simulaciones.txt')


"""
pos = 0
accepted = False
flag = True
print('regex: ', exp)
print('test: ', dummy_test)
while flag:
    #print('Current state: ', current_state.name)
    #print('Current char: ', dummy_test[pos])
    if dummy_test[pos] in current_state.transitions:
        current_state = current_state.transitions[dummy_test[pos]]
        pos += 1
    else:
        flag = False
    #print('-'*50)
    if pos == len(dummy_test) and current_state.isAccept:
        accepted = True
        flag = False

if accepted:
    print(' - String accepted')
else:
    print(' - String not accepted')
"""
"""print(' / ' * 50)

for e in AFD_directo:
    print(e)
    print(e.name, e.isAccept, e.transitions)
    print(e.contains)
    print(e.isInitial)
    print(' - ' * 50)

print(' / ' * 50)



for e in AFD_directo_minimizado:
    print(e)
    print(e.name, e.isAccept, e.transitions)
    print(e.contains)
    print(e.isInitial)
    print(' - ' * 50)

print(' - ' * 50)
"""


# cual = 4
# 
# AFN, AFD_de_AFN, AFD_directo, AFD_minimizado, AFD_directo_minimizado, arbol, exp = main(exps[cual])
# #visualRepresentation(AFN, AFD_de_AFN, AFD_directo, AFD_minimizado, AFD_directo_minimizado, arbol, exp)
# dummy_test = strings[cual][0]
# print('Cadena de prueba: ' + dummy_test + '\n')
# print(' / ' * 50)
# AFD_result, bitacora = simulation(AFD_de_AFN[0], dummy_test)
# bitacora += ' - Cadena aceptada? ' + str(AFD_result)
# print(bitacora)
# print('AFD de AFN: ')
# print(' - ', AFD_result)
# print()
# AFD_d_result, bitacora = simulation(AFD_directo[0], dummy_test)
# bitacora += ' - Cadena aceptada? ' + str(AFD_d_result)
# print(bitacora)
# print('AFD directo: ')
# print(' - ', AFD_d_result)
# print()
# AFD_min_result, bitacora = minimizedSimulation(AFD_minimizado, dummy_test)
# bitacora += ' - Cadena aceptada? ' + str(AFD_min_result)
# print(bitacora)
# print('AFD minimizado: ')
# print(' - ', AFD_min_result)
# print()
# AFD_directo_min_result, bitacora = minimizedSimulation(AFD_directo_minimizado, dummy_test)
# bitacora += ' - Cadena aceptada? ' + str(AFD_directo_min_result)
# print(bitacora)
# print('AFD directo minimizado: ')
# print(' - ', AFD_directo_min_result)