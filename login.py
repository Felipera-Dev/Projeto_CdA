 #Feito por Felipe da Veiga Gomes e Rogerio Abreu
import json

def LerDadosUser():
    with open('usuarios.json') as file:
        data = json.load(file)
        return data

def LerDadosPerm():
    with open('permissoes.json') as filePerm:
        dataPerm = json.load(filePerm)
        return dataPerm

def cadastrar():
    user = input("Digite seu nome:")
    senha = input("Digite sua senha:")

    usuarios = {
        "user": user,
        "senha":senha
    },
    permissoes = {
        "user": user,
        "permissoes": [
            {
                "arquivo": "teste.png",
                "ler":False,
                "escrever":False,
                "excluir":False
            }
        ]
    }

    dadosUser = LerDadosUser()
    dadosUser.append(usuarios)

    dadosPerm = LerDadosPerm()
    dadosPerm.append(permissoes)
    
    json_string = json.dumps(dadosUser, indent=4)
    with open('usuarios.json', 'w') as arquivo:
        arquivo.write(json_string)

    json_string_perm = json.dumps(dadosPerm, indent=4)
    with open('permissoes.json', 'w') as arquivoPerm:
        arquivoPerm.write(json_string_perm)

    print("Cadastro Concluido")

def login():
    user_login = input("Digite seu nome:")
    senha_login = input("Digite sua senha:")


    usuarios = LerDadosUser()

    achou_user = False
    achou_senha = False
    for user in usuarios:
        user_registrado = user["user"]
        senha_registrada = user["senha"]

        if user_registrado == user_login:
            if senha_registrada == senha_login:
                achou_user = True
                achou_senha = True


    if achou_senha and achou_user:
        print("Seja bem vindo", user_login)

        # opcaologin = 0
        # while opcaologin != 5:
        #     opcaologin = input(" 1 - Listar Arquivos | 2 - Ler Arquivo | 3 - Escrever Arquivo | 4 - Excluir Arquivo  | 5 - Sair  ")
    else:
        print("Nome ou Senha incorretos")

opcao = 0
while opcao != "4":
    opcao = input(" 1 - Cadastro | 2 - Login | 3 - Sair:")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()

