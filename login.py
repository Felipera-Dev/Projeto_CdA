 #Feito por Felipe da Veiga Gomes e Rogerio de Abreu Mar
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
    }
    permissoes = {
        "user": user,
        "permissoes": [
            {
                "arquivo": "foto.png",
                "ler":False,
                "escrever":False,
                "excluir":False
            },
            {
                "arquivo": "codigo.c",
                "ler":False,
                "escrever":False,
                "excluir":False
            },
            {
                "arquivo": "arquivo.bat",
                "ler":False,
                "escrever":False,
                "excluir":False
            }
        ]
    }

    dadosUser = LerDadosUser()
    for user_cadastro in dadosUser:
     if user == user_cadastro["user"]:
        print("Usuário já cadastrado")
        return
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

        opcaologin = 0
        while opcaologin != "5":
            opcaologin = input(" 1 - Listar Arquivos | 2 - Ler Arquivo | 3 - Escrever Arquivo | 4 - Excluir Arquivo  | 5 - Sair  ")
            if opcaologin == "1":
                print("Listar Arquivos")
                ListarArquivos()
            elif opcaologin == "2":
                VerificarPerm(user_login, "ler")   
            elif opcaologin == "3":
                VerificarPerm(user_login, "escrever")   
            elif opcaologin == "4":
                VerificarPerm(user_login, "excluir")                        
            else:
                print("Opção inválida")
    else:
        print("Nome ou Senha incorretos")

def ListarArquivos():
    dadosPerm = LerDadosPerm()
    arquivos_set = set() # Usando um set para evitar duplicar arquivos 

    for user in dadosPerm:
        for permissao in user["permissoes"]:
            arquivos_set.add(permissao["arquivo"])

    print("Arquivos:")
    for arquivo in arquivos_set:
        print(arquivo)
        
def VerificarPerm(user_login, acao):
    dadosPerm = LerDadosPerm()
    print(acao,"arquivo------------------------------------------")
    arquivo = input("Digite o nome do arquivo:")
    achou_arquivo = False
    for user in dadosPerm:
        if user["user"] == user_login:
            for permissao in user["permissoes"]:
                  if permissao["arquivo"] == arquivo:
                    achou_arquivo = True
                    if permissao[acao] == True:
                        print(f"Você pode {acao} o arquivo",    permissao["arquivo"] )
                        
                    else:
                        print(f"Você não pode {acao} o arquivo", permissao["arquivo"]) 
                        
    if achou_arquivo == False:
        print("Arquivo não encontrado")	
    print("-----------------------------------------------------")    
                    
                        
opcao = 0
while opcao != "3":
    opcao = input(" 1 - Cadastro | 2 - Login | 3 - Sair:")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Saindo do sistema...")
    else:
        print("Opção inválida")

