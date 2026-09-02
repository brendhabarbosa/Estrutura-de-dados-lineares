from pilhas import pilha

expression = input("Digite a expressão: ")

pilha_expression = pilha.Pilha()
balanceada = True

for caractere in expression:
    if caractere == "(" or caractere == "[" or caractere == "{":
        pilha_expression.push(caractere)
    elif caractere == ")" or caractere == "]" or caractere == "}":
        if pilha_expression.is_empty():
            balanceada = False
            break
        if caractere == ")" and pilha_expression.top() == "(":
            pilha_expression.pop()
        elif caractere == "]" and pilha_expression.top() == "[":
            pilha_expression.pop()
        elif caractere == "}" and pilha_expression.top() == "{":
            pilha_expression.pop()      
        else:
            balanceada = False
            break

if not pilha_expression.is_empty():
    balanceada = False
    

if balanceada:
    print("Expressão balanceada")
else:
    print("Não está balanceada")
