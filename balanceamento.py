from pilhas import pilha

expression = input("Digite a expressão: ")

pilha_expression = pilha.Pilha()
balanceada = True
lista_invalidos = []

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
            lista_invalidos.append(caractere)
            break

count_abertos = 0
count_fechados = 0

if not pilha_expression.is_empty():
    balanceada = False
    for i in lista_invalidos:
        if i == "(" or i == "[" or i == "{":
            count_abertos += 1
        elif i == ")" or i == "]" or i == "}":
            count_fechados += 1

if balanceada:
    print("Expressão balanceada")
else:
    print("Não está balanceada")
    print("Inválidos:\nNúmero de aberturas: ", count_abertos)
    print("Número de fechamentos: ", count_fechados)
