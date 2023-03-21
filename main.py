from crud_cliente import *
import os

print("--------------")
print("BEM VINDO")
print("--------------")
print("1- USUARIO")
print("2- VENDEDOR")
print("3- PRODUTOS")
print("4- COMPRAS")
print("--------------")
tabela_selecionada = input("Selecione a tabela que deseja utilizar: ")


match tabela_selecionada:
    case "1":
        os.system('cls')
        print("--------------")
        print("TABELA DE USUARIO:")
        print("1- CRIAR")
        print("2- MOSTRAR TODOS")
        print("3- ATUALIZAR")
        print("4- DELETAR")
        print("--------------")

        funcao_selecionada = input("Selecione o que deseja fazer: ")

        if (funcao_selecionada == "1"):
            print("Cadastrando Usuário")
            nome_cadastro = input("Digite o nome do usuario: ")
            email_cadastro = input("Digite o email: ")
            cpf_cadastrado = input("Digite o cpf: ")
            
            print("Endereço: ")
            logradouro = input("Digite o nome da rua: ")
            numero = input("Digite o número: ")
            bairro = input("Digite o bairro: ")
            endereco_cadastrado = {"logradouro":logradouro,"numero":numero,"bairro":bairro}

            print("Favoritos")
            id_produto = input("Digite o id do produto: ")
            nome_produto = input("Digite nome do produto: ")
            favoritos_cadastrado = {"id_produto":id_produto, "nome_produto":nome_produto}

            Cliente_insert(nome_cadastro, email_cadastro, endereco_cadastrado, favoritos_cadastrado, cpf_cadastrado)
     
        elif (funcao_selecionada == "2"):
            Cliente_searchAll()

        elif (funcao_selecionada == "3"):
            print("Atualizando usuario")
            print("Cadastrando um novo endereço: ")
            cpf = input("Digite o cpf do cliente que deseja cadastrar um novo endereco: ")



            novo_logradouro = input("Digite o novo nome da rua: ")
            novo_numero = input("Digite novo o número: ")
            novo_bairro = input("Digite novo o bairro: ")
            novo_endereco_cadastrado = {"logradouro":novo_logradouro,"numero":novo_numero,"bairro":novo_bairro}

            Cliente_Update(cpf,novo_endereco_cadastrado)

        elif(funcao_selecionada == "4"):
            print("Deletar usuario")
            cpf = input("Digite o cpf do usuario que deseja deletar: ")
            Cliente_deleteOne(cpf)












    case "2":
        os.system('cls')
        print("--------------")
        print("TABELA DE VENDEDOR:")
        print("1- CRIAR")
        print("2- MOSTRAR TODOS")
        print("3- ATUALIZAR")
        print("4- DELETAR")
        print("--------------")
        



        










    case "3":
        os.system('cls')
        print("--------------")
        print("TABELA DE PRODUTOS:")
        print("1- CRIAR")
        print("2- MOSTRAR TODOS")
        print("3- ATUALIZAR")
        print("4- DELETAR")
        print("--------------")











    case "4":
        os.system('cls')
        print("--------------")
        print("TABELA DE COMPRAS:")
        print("1- CRIAR")
        print("2- MOSTRAR TODOS")
        print("3- ATUALIZAR")
        print("4- DELETAR")
        print("--------------")


    case _:
        print("Selecione uma opção existente!")
    