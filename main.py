from InfixToPostfix import InfixToPostfix
from AFN import generateAFN, visual_AFN

#exp = '(a|b)*a(a|b)(a|b)'

#exp = 'a**(b|c)?*(da+)?a(c|d*)+'

# input de la expresión regular
exp = input("Ingrese la expresión regular: ")


exp_postfix = InfixToPostfix(exp)

if exp_postfix == False:
    print("Expresión regular inválida")
    exit()

postfix = ''.join(exp_postfix)
print("Expresión regular formato postfix: ", postfix)
AFN = generateAFN(exp_postfix)  
visual_AFN(AFN)