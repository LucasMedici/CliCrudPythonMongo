import pymongo


client = pymongo.MongoClient("mongodb+srv://LucasMedici:Lucci1203@nomedocluster.ip8jntw.mongodb.net/?retryWrites=true&w=majority")
mydb = client.MercadoLivre



# Create
def Produto_insert(nome, id_vendedor, qnt, preco, id_produto): 
    global mydb
    mycol = mydb.produtos
    mydict = {"nome": nome, "id_vendedor": id_vendedor, "qnt":qnt, "preco":preco, "id_produto":id_produto}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


# Find all
def Produto_searchAll():
    global mydb
    mycol = mydb.produtos
    mydoc = mycol.find().sort("nome")
    for a in mydoc:
        print(a)


# Delete
def Produto_deleteOne(id_produto):
    global mydb
    mycol = mydb.produtos
    myquery = {"id_produto":id_produto}
    mycol.delete_one(myquery)




#Update
def Produto_update(id_produto, qnt_nova):
    global mydb
    mycol = mydb.produtos
    myquery = {"id_produto": id_produto}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
        novo_valores = {"$set": {"qnt": qnt_nova}}


        mycol.update_one(myquery, novo_valores)