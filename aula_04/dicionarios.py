usuarios={} # dicionário de dados
usuarios={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
    }
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"] # adição de outro objeto

print(usuarios)
print("##############========#########")
print("Dados: ",usuarios.get("Chaves")) # retorna os dados que estão dentro da chave "Chaves"
# usuarios={}
# usuarios={
#     "Chaves":["Chaves Silva","17/06/1975","Recep_01"],
#     "Quico":["Enrico Flores","03/06/1976","Raiox_02"],
#     "Quico":["Enrico Flores","03/06/1976","Raiox_03"] # caso repetir os dados, o segundo ira sobreescrever o primeiro
#     }
# usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
# usuarios["Florinda"]=["Florinda Flores", "26/11/2016", "Recep_01"]
# print (usuarios)

