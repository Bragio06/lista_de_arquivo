with open('estudantes.txt','w') as dados:
    resp = 1

    dados_do_estudantes = {}

    while resp != 0 :
        estudante_curso = input("digite o curso do estudante: ")
        estudante_nome = input("digite o nome do estudante: ")
        estudante_idade = input("digite a idade do estudante: ")

        dados_do_estudantes['nome'] = estudante_nome
        dados_do_estudantes['idade'] = estudante_idade
        dados_do_estudantes['curso'] = estudante_curso

        dados.write(f"{dados_do_estudantes}\n")

        resp = int(input("digite 1 se deseja continuar: \ndigite 0 se deseja parar: \n"))