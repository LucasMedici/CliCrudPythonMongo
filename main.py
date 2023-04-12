from crud_cliente import *
from crud_produto import *
from crud_vendedor import *
from crud_compras import *
import redisConection
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
            os.system('cls')
            print("###Atualizando um cliente###")
            print("1- Cadastrar favoritos pelo REDIS")
            print("2- Cadastrar enderecos pelo REDIS")
            opcao = input("Digite a opção que deseja selecionar: ")
            if(opcao == "1"):
                redisConection.AddFavsPeloRedis()              
            elif(opcao == "2"):
                redisConection.AddEnderecoPeloRedis()
            else:
                print('número inválido!')
            

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


        funcao_selecionada = input("Selecione o que deseja fazer: ")

        if (funcao_selecionada == "1"):
            print("Cadastrando Vendedor")
            nome_cadastro = input("Digite o nome do vendedor: ")
            email_cadastro = input("Digite o email: ")
            print("Produtos: ")

            
            nome_produto_vendedor = input("Digite o nome do produto : ")
            qnt_produto_vendedor = input("Digite a quantidade: ")
            preco_produto_vendedor = input("Digite o preço: ")
            produto_vendedor = {"nome":nome_produto_vendedor,"qnt":qnt_produto_vendedor,"preco":preco_produto_vendedor}

            id_cadastro = input("Digite o id do vendedor: ")

            vendedor_insert(nome_cadastro, email_cadastro, produto_vendedor, id_cadastro)
     


        elif (funcao_selecionada == "2"):
            vendedor_searchAll()

        elif (funcao_selecionada == "3"):
            print("Atualizando vendedor")
            print("Cadastrando um novo produto: ")
            id_vendedor = input("Digite o id do vendedor que deseja cadastrar um novo produto: ")



            novo_nome_produto_vendedor = input("Digite o nome do produto : ")
            novo_qnt_produto_vendedor = input("Digite a quantidade: ")
            novo_preco_produto_vendedor = input("Digite o preço: ")
            novo_produto_vendedor = {"nome":novo_nome_produto_vendedor,"qnt":novo_qnt_produto_vendedor,"preco":novo_preco_produto_vendedor}

            vendedor_Update(id_vendedor,novo_produto_vendedor)

        elif(funcao_selecionada == "4"):
            print("Deletar vendedor")
            id_vendedor = input("Digite o id do vendedor que deseja deletar: ")
            vendedor_deleteOne(id_vendedor)
        



        










    case "3":
        os.system('cls')
        print("--------------")
        print("TABELA DE PRODUTOS:")
        print("1- CRIAR")
        print("2- MOSTRAR TODOS")
        print("3- ATUALIZAR")
        print("4- DELETAR")
        print("--------------")


        funcao_selecionada = input("Selecione o que deseja fazer: ")

        if (funcao_selecionada == "1"):
            print("Cadastrando Produtos")
            nome_cadastro = input("Digite o nome do produto: ")
            id_vendedor = int(input("Digite o id do vendedor do produto: "))
            qnt = int(input("Digite a quantidade do produto: "))
            preco = float(input("Digite o preço do produto: "))
            id_produto = input("Digite o id do produto: ")
        
            Produto_insert(nome_cadastro, id_vendedor, qnt, preco, id_produto)
     
        elif (funcao_selecionada == "2"):
            Produto_searchAll()

        elif (funcao_selecionada == "3"):
            print("Atualizando produto")
            print("Alterando a quantidade: ")
            id_produto = input("Digite o id do produto que deseja alterar a quantidade: ")



            nova_quantidade = int(input("Digite a nova quantidade: "))
            Produto_update(id_produto,nova_quantidade)
            

            

        elif(funcao_selecionada == "4"):
            print("Deletar Produto")
            id_produto = input("Digite o id do produto que deseja deletar: ")
            Produto_deleteOne(id_produto)












    case "4":
        os.system('cls')
        print("--------------")
        print("TABELA DE COMPRAS:")
        print("1- CRIAR")
        print("2- MOSTRAR TODOS")
        print("3- DELETAR")
        print("--------------")





        funcao_selecionada = input("Selecione o que deseja fazer: ")

        if (funcao_selecionada == "1"):
            print("Cadastrando Compras")
           
            id_usuario = input("Digite o id do comprador: ")
            id_vendedor = input("Digite o id do vendedor: ")

            print("Especificando Produto da compra")

            nome_produto = input("Digite o nome do produto : ")
            id_produto = input("Digite o id do produto: ")
            preco_produto = input("Digite o preço: ")
            qnt = input("Digite a quantidade: ")
            produto_da_compra = {"nome_produto":nome_produto,"id_produto":id_produto,"preco_produto":preco_produto, "qnt":qnt}
            
            id_compra = input("Digite o id da compra: ")
        
            compras_insert(id_usuario, id_vendedor, produto_da_compra, id_compra)
     
        elif (funcao_selecionada == "2"):
            compras_searchAll()
   

        elif(funcao_selecionada == "3"):
            print("Deletar Compras")
            id_compra = input("Digite o id da compra que deseja deletar: ")
            compras_deleteOne(id_compra)


    case _:
        print("Selecione uma opção existente!")
    