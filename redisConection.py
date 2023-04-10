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


favoritos_em_string = json.dumps((obj_cliente['favoritos']),cls=MongoEncoder)

def sincronizandoRedis():
    conR.delete('favoritos')
    conR.set('favoritos', favoritos_em_string)
        
        
def novoFavorito():
    os.system('cls')
    print('### CADASTRANDO UM NOVO FAVORITO ###')
    id_novofavorito = input("Digite o ID do novo favorito: ")
    nome_novofavorito = input("Digite o nome do novo favorito: ")
    novo_favorito = {"id_produto":id_novofavorito,"nome_produto":nome_novofavorito}
    

    favoritos_no_redis = str(conR.get('favoritos'))
    
    favoritos_formatados = favoritos_no_redis[1:(-1)-1]

    novos_favoritos = f"{favoritos_formatados}, {novo_favorito}]"
    novos_favoritos = novos_favoritos.replace("'", '"')
    novos_favoritos = novos_favoritos.replace("[","")
    novos_favoritos = novos_favoritos.replace("]","")
    print(novos_favoritos)
   

    jsonzada = json.loads(novos_favoritos)
    print(jsonzada)


   

sincronizandoRedis()
novoFavorito()
# CRIAR FUNCAO PARA ATT MONGO atualizandoMongo()



# conR.set('favoritos', novo_favorito)


# print(conR.get('user:name'))