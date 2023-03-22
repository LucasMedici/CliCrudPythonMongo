
import pymongo


client = pymongo.MongoClient("mongodb+srv://LucasMedici:Lucci1203@nomedocluster.ip8jntw.mongodb.net/?retryWrites=true&w=majority")
mydb = client.MercadoLivre


# Create
def vendedor_insert(nome, email, produtos,id_vendedor):
    global mydb
    mycol = mydb.vendedor
    mydict = {"nome": nome, "email": email, "produtos":[produtos], "id_vendedor":id_vendedor}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


# Find by id
def vendedor_findQuery():
    global mydb
    mycol = mydb.vendedor
    myquery = {"id_vendedor": "1"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)



# Find all
def vendedor_searchAll():
    global mydb
    mycol = mydb.vendedor
    mydoc = mycol.find().sort("nome")
    for a in mydoc:
        print(a)

# Delete
def vendedor_deleteOne(id_vendedor):
    global mydb
    mycol = mydb.vendedor
    myquery = {"id_vendedor":id_vendedor}
    mycol.delete_one(myquery)


#Update
def vendedor_Update(id_vendedor,novo_produto):
    global mydb
    mycol = mydb.vendedor
    myquery = {"id_vendedor": id_vendedor}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        x["produtos"].append(novo_produto)
        produtos_salvos = x["produtos"]
        novo_valores = {"$set": {"produtos": [produtos_salvos]}}


        mycol.update_one(myquery, novo_valores)


