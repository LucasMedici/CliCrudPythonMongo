
import pymongo


client = pymongo.MongoClient("mongodb+srv://LucasMedici:Lucci1203@nomedocluster.ip8jntw.mongodb.net/?retryWrites=true&w=majority")
mydb = client.MercadoLivre


# Create
def Cliente_insert(nome, email, endereco,favoritos,cpf):
    global mydb
    mycol = mydb.usuario
    mydict = {"nome": nome, "email": email, "endereco":[endereco], "favoritos":[favoritos], "cpf":cpf}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


# Find by id
def Cliente_findQuery(cpf):
    global mydb
    mycol = mydb.usuario
    myquery = {"cpf": cpf}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
    return x



# Find all
def Cliente_searchAll():
    global mydb
    mycol = mydb.usuario
    mydoc = mycol.find().sort("nome")
    for a in mydoc:
        print(a)

# Delete
def Cliente_deleteOne(cpf):
    global mydb
    mycol = mydb.usuario
    myquery = {"cpf":cpf}
    mycol.delete_one(myquery)


#Update
def Cliente_Update(cpf,novo_endereco):
    global mydb
    mycol = mydb.usuario
    myquery = {"cpf": cpf}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        x["endereco"].append(novo_endereco)
        enderecos_salvos = x["endereco"]
        print(enderecos_salvos)
        novo_valores = {"$set": {"endereco": [enderecos_salvos]}}


        mycol.update_one(myquery, novo_valores)


