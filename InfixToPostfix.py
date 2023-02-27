from BinaryTree import buildTree, ArrayInArray
#from AFN import generateAFN

# Métodos de transfroemación infix a postfix utilizando shunting yard

exp = []
operators = ['*', '|', '.', '(', ')']
# extra operators: ?, +

ops = {'*': 3, '.': 2, '|': 1}



# Transformar los operdores abreviados a su forma completa
# Ejemplo: a*b?c -> a*(b|ε)c
# Ejemplo: a*b+c -> a*(bb*)+c
# versión mejorada de la función translate
def trans(exp):
    # el recorrido se hace de derecha a izquierda para evitar problemas con los índices
    i = len(exp) - 1
    while i >= 0:
        temp = exp[i]
        if exp[i] == '*':
            if exp[i-1] == '*':
                j = i 
                while exp[j] == '*':
                    j -= 1
                exp = exp[:j+1] + exp[i:]
                i = j+1
                #print(exp)
        elif exp[i] == '?':
            if exp[i-1] == ')':
                j = i
                while exp[j] != '(':
                    j -= 1
                exp2 = exp[j:i]
                exp = exp[:j] + '(' + exp2 + '|ε)' + exp[i+1:]
                i = j+1
            else:
                exp = exp[:i-1] + '(' + exp[i-1] + '|ε)' + exp[i+1:]
        elif exp[i] == '+':
            if exp[i-1] == ')':
                j = i
                while exp[j] != '(':
                    j -= 1
                exp2 = exp[j:i]
                exp3 = exp[:j]
                exp = exp[:j] + '(' + exp2 + exp2 + '*' + ')' + exp[i+1:]
                i = j+1
            else:
                exp = exp[:i-1] + '(' + exp[i-1] + exp[i-1] + '*' + ')' + exp[i+1:]
        i -= 1
    flag = False
    for e in exp:
        if e == '+' or e == '?':
            flag = True
    if flag:
        exp = trans(exp)
    return exp




# Primera función de validación de la expresión regular
# Verifica que los paréntesis estén balanceados, de otra forma
# no se puede realizar la transformación y se debe indicar al usuario
# que la expresión regular no es válida
def parenthesis_check(exp):
    acu = 0
    open_parenthesis = False
    for e in exp:
        if e == '(':
            acu += 1
            open_parenthesis = True
        elif e == ')':
            acu -= 1
            open_parenthesis = False
    if acu == 0 and not open_parenthesis:
        return True
    else:
        return False


# Segunda función de validación de la expresión regular
# Verifica que la expresión regular no contenga caracteres inválidos
# de otra forma no se puede realizar la transformación y se debe indicar al usuario
# que la expresión regular no es válida
def syntax_check(exp):
    pass


# Tercera función de validación de la expresión regular
# Verifica que la expresión regular no contenga errores de gramática
# de otra forma no se puede realizar la transformación y se debe indicar al usuario
# que la expresión regular no es válida

# SE HARÁ EL CHEQUEO ANTES DE REALIZAR LA TRANSFORMACIÓN DE SÍMBOLOS ABREVIADOS
# A SU FORMA COMPLETA
# ESTO CON EL OBJETIVO DE AHORRAR TIEMPO DE EJECUCIÓN SIENDO QUE LOS SÍMBOLOS	
# ABREVIADOS, SIENDO UNARIOS, SON MÁS FÁCILES DE IDENTIFICAR QUE LOS OPERADORES
# BINARIOS

# Caso 1: No alimentarle las entradas necesarias a los operadores unarios y binarios
# Caso 2: Alimentarle a un operador binario una entrada que no sea un símbolo o un paréntesis o un operador binario
def grammar_check(exp):
    pass
    


#Función necesaria para leer la expresión regular y agregar los operadores de concatenación
def readExp(exp):
    infix = []
    abc = [] 
    symbols = ['*', '|', '(', ')']
    #exp = input('Ingrese la expresion regular: \n')
    exp2 = ''
    for e in exp:
        infix.append(e)
        if e not in symbols and e not in abc:
            abc.append(e)
    size = len(infix)
    kleene = False
    waiting  = 0
    while size > 0:
        if size > 1:
            v1 = infix[size-1]
            v2 = infix[size-2]
            if kleene:
                if waiting > 0:
                    waiting -= 1
                    kleene = False                    
                    waiting = 0
            elif v1 == '*' and not kleene:
                kleene = True
                waiting = 1
            if (v1 == '(' and v2 in abc and not kleene) or (v1 in abc and v2 == ')' and not kleene) or (v1 in abc and v2 in abc and not kleene) or (v1 == '(' and v2 == ')' and not kleene) or (v1 in abc and v2 == '*' and not kleene) or (v1 == '(' and v2 == '*' and not kleene):
                exp2 = '.' + v1 + exp2
            else:
                exp2 = v1 + exp2
            size -= 1
        else:
            v1 = infix[size-1]
            exp2 = v1 + exp2
            size -= 1
    #exp2 = exp2 + '.#'
    return exp2


#Basado en el algortimo de Shunting-yard
def InfixToPostfix(exp):
    exp = trans(exp)
    if parenthesis_check(exp):
        exp = readExp(exp)
        #print(exp)
        OpStack = []
        postfix = []
        for e in exp:
            #If the input symbol is a letter… append it directly to the output queue
            if e not in operators:
                postfix.append(e)
            else:
                if e == '(':
                    OpStack.append(e)
                elif e == ')' and OpStack[-1] != '(' and len(OpStack) > 0:
                    while OpStack[-1] != '(':
                        postfix.append(OpStack.pop())
                    OpStack.pop()
                else:
                    if len(OpStack) > 0:
                        while len(OpStack) > 0 and OpStack[-1] != '(' and ops[e] <= ops[OpStack[-1]]:
                            postfix.append(OpStack.pop())
                    OpStack.append(e)
        while len(OpStack) > 0:
            postfix.append(OpStack.pop())
        #postfix.append('#')
        #postfix.append('.')
        #exp_postfix = ''.join(postfix)
        #return exp_postfix
        return postfix
    else:
        return 'La expresión regular no es válida, verifique que los paréntesis estén balanceados'


# expresiones regulares de prueba válidas en forma expandida, no concatenadas
#exp = 'abc'
# exp = 'a|b'
# exp = 'a|b|c'
# exp = '(a|b)*'s
# exp = '(a|b)*c'
# exp = '(a|b*)**cd'
#exp  = 'a**b*c|d'

#exp = '(a|b)*abb(a|b)*'

# expresiones regulares de prueba válidas en forma abreviada
#exp = 'a*b?**c+'
#exp = 'a*b+c'
#exp = 'a*b+c*'
#exp = 'a*b+c*|d'
#                     exp = 'a**(b|c)?*(da+)?a(c|d*)+'
#exp = '(a?|b+)***c**'
#exp = '(a|b+)+'
#exp = '(a***|b****)***'
#exp = '(a|b)*abb'


# expresiones regulares de prueba inválidas
#exp = ')a|b('

#print('Expresión regular: ', exp)
#print('Expresión regular en forma abreviada: ', translate(exp))
#print('Expresión simplificada: ', trans(exp))
#sprint(parenthesis_check(exp))



#exp = InfixToPostfix(exp)
#
#
#print('Expresión regular postfix: ', exp)
#for e in exp: 
 #   print(e)
##### exp = list(exp)
##### syntactic_tree = buildTree(exp.pop(), exp)
##### 
##### 
##### 
##### print('\n\n')
##### 
##### print('Árbol sintáctico: ', syntactic_tree)
##### print(syntactic_tree.traversePostOrder())#
##### print('\n\n')
##### syntactic_tree.post2()
##### syntactic_tree.determineFollowPos()
##### 
#syntactic_tree.post3()
#syntactic_tree.post2()
#syntactic_tree.determineFollowPos()
#syntactic_tree.post3()
#
##print('Expresión regular 2: ', InfixToPostfix(exp))
#