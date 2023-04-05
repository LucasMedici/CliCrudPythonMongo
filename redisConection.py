import redis
import os
import json
from bson import ObjectId

from crud_cliente import *;



conR = redis.Redis(
  host='redis-13523.c14.us-east-1-3.ec2.cloud.redislabs.com',
  port=13523,
  password='C2JYyEBusx1c6TUlzgzP8zVfKa5ksi7j')


print("### CADASTRANDO UM NOVO FAVORITO NO REDIS ###")
cpf_usuario = input("Digite o CPF do usuario que deseja cadastrar um novo favorito: ")
obj_cliente = Cliente_findQuery(cpf_usuario)

class MongoEncoder(json.JSONEncoder):
    def default (self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


obj_em_string = json.dumps((obj_cliente),cls=MongoEncoder)
print(obj_em_string)


def sincronizandoRedis():

    conR.set('chave', obj_em_string)
    # i=0
    # for a in obj_cliente['favoritos']:
    #     conR.lpush('lista_favoritos', obj_cliente['favoritos'][i]['id_produto'], obj_cliente['favoritos'][i]['nome_do_produto'])
    #     i+=1
        

sincronizandoRedis()
print(conR.get('chave'))
# print(conR.get('nome_Da_lista'))

# os.system('cls')
# print("### CADASTRANDO UM NOVO FAVORITO ###")
# id_novofavorito = input("Digite o ID do novo favorito: ")
# nome_novofavorito = input("Digite o nome do novo favorito: ")

# novo_favorito = {"id_produto":id_novofavorito, "nome_produto":nome_novofavorito}

# conR.set('favoritos', novo_favorito)


# print(conR.get('user:name'))