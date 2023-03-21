import pymongo


client = pymongo.MongoClient("mongodb+srv://LucasMedici:Lucci1203@nomedocluster.ip8jntw.mongodb.net/?retryWrites=true&w=majority")
mydb = client.MercadoLivre



# Create
def Produto_insert(nome, id_vendedor, qnt, preco): 
    global mydb
    mycol = mydb.produtos
    mydict = {"nome": nome, "id_vendedor": id_vendedor, "qnt":qnt, "preco":preco}
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
def Cliente_deleteOne(_id):
    global mydb
    mycol = mydb.produtos
    myquery = {"_id":_id}
    mycol.delete_one(myquery)