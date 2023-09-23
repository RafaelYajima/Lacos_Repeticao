#Lista de alunos e suas medias

alunos = []
notas = []
solicita_notas = True

while solicita_notas:
    aluno = input("Digite o nome do aluno: ")
    alunos.append(aluno)

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    notas_aluno = (n1, n2, n3, n4)
    notas.append(notas_aluno)

    continua = input("Deseja continuar? (S/N) ")
    if continua == "N": solicita_notas = False

for aluno in alunos:
    print("Aluno: ",aluno)
    notas_aluno = notas[alunos.index(aluno)]
    quantidade_notas = len(notas_aluno)
    
    soma = 0
    for nota in notas_aluno:
        soma += nota
        print("Nota: ", nota)

    media = soma / quantidade_notas
    
    print("A media é:",media)