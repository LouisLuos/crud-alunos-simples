import json
import os
alunos = []

caminho = "alunos.json"



def salvar_json(alunos, caminho):
    try:
        with open(caminho, "w", encoding='utf-8') as arq:
            json.dump(alunos, arq, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Ocorreu um erro {e} no seu código")


def carregar_usuarios():
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding='utf-8') as arq:
                return json.load(arq)
            
        except json.JSONDecodeError:
            return []


def criar_aluno():
    alunos = carregar_usuarios()
    aluno = {}
    aluno["nome"] = input("Digite seu nome: ") 
    aluno["idade"] = int(input("Digite sua idade: ").strip())
    aluno["nota"] = float(input("Digite sua nota: ").strip()) 
    alunos.append(aluno.copy())
    salvar_json(alunos, caminho)
    print(f"Aluno: {aluno["nome"]} criado com sucesso!")

def listar_aluno():
    lista_de_alunos = carregar_usuarios()
    if not carregar_usuarios():
         
        print("Não existe alunos cadastrados")
    else:
        for aluno in lista_de_alunos:
            print(f"Aluno: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")



def buscar_aluno():
    lista_de_alunos = carregar_usuarios()
    nome_buscar = input("Qual nome do aluno deseja procurar?")
    try:
        for aluno in lista_de_alunos:
            if nome_buscar == aluno['nome']:
                print(f"Esses são os dados do aluno buscado: Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")

                      
    except:
        print("Não há usuário cadastrados")


def atualizar_nota():
    lista_de_alunos = carregar_usuarios()
    nome_buscar = input("Qual nome do aluno que deseja alterar a nota?")
    nota_nova = input("Qual é a nota nova?")
    encontrou = False
    for aluno in lista_de_alunos:
        if nome_buscar == aluno["nome"]:
            aluno['nota'] = nota_nova
            encontrou = True
            print(f"A nota nova atribuida ao aluno foi {aluno['nota']}")
    
    if encontrou:
        salvar_json(lista_de_alunos, caminho)



def media_geral():
    lista_de_alunos = carregar_usuarios()
    total_alunos = len(lista_de_alunos)
    print(f'Total de alunos: {total_alunos}')

    soma_notas = 0.0
    nota_alunos = []

    for a in lista_de_alunos:
        nota = float(a['nota'])
        nota_alunos.append(nota)
        soma_notas = soma_notas + nota
        
    media_total = soma_notas / total_alunos
    print(f"A média total é {media_total:.2f}")
        
        

def menu_principal():
    while True:
        print("1 - Criar alunos")
        print("2 - Listar alunos")
        print("3 - Buscar alunos")
        print("4 - Atualizar nota de alunos")
        print("5 - Calcular média geral")
        print("6 - Encerrar programa")
        
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print('-' * 50)
            criar_aluno()
            print('-' * 50)

        elif opcao == 2:
            print('-' * 50)
            listar_aluno()
            print('-' * 50)

        elif opcao == 3:
            print('-' * 50)
            buscar_aluno()
            print('-' * 50)

        elif opcao == 4:

            print('-' * 50)
            atualizar_nota()
            print('-' * 50)

        elif opcao == 5:

            print('-' * 50)
            media_geral()
            print('-' * 50)

        elif opcao == 6:
            print('-' * 50)
            print("Encerrando programa")
            print('-' * 50)
            break


if __name__ == "__main__":
    menu_principal()





