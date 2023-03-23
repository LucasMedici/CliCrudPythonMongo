

import pymongo


client = pymongo.MongoClient("mongodb+srv://LucasMedici:Lucci1203@nomedocluster.ip8jntw.mongodb.net/?retryWrites=true&w=majority")
mydb = client.MercadoLivre


def compras_insert(id_usuario, id_vendedor, produto_da_compra, id_compra):
    global mydb
    mycol = mydb.compras
    mydict = {"id_usuario":id_usuario, "id_vendedor":id_vendedor, "produto_da_compra":produto_da_compra, "id_compra":id_compra}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)



def compras_searchAll():
    global mydb
    mycol = mydb.compras
    mydoc = mycol.find().sort("id_usuario")
    for a in mydoc:
        print(a)


def compras_deleteOne(id_compra):
    global mydb
    mycol = mydb.compras
    myquery = {"id_compra": id_compra}
    mycol.delete_one(myquery)