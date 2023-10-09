with open('estudantes.txt','r') as dados:
    nome = input("qual o nome do estudante: ")
    for linha in dados:
        if nome in linha:
            print(linha)