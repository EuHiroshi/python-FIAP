# lista_estatica = ["xpto", True] #lista preenchida estaticamente
# lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))] #lista preenchida dinamicamente
# lista_vazia=[] #lista vazia

# print(lista_dinamica)


# inventario=[]
# resposta="S"
# while resposta=="S":
#   inventario.append(input("Equipamento: "))
#   inventario.append(float(input("Valor: ")))
#   inventario.append(int(input("Número Serial: ")))
#   inventario.append(input("Departamento: "))
#   resposta=input("Digite 'S' para continuar: ").upper()

# for elemento in inventario:
#   print(elemento)

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  # seriais.append(int(input("Número Serial: ")))
  # departamentos.append(input("Departamento: "))
  resposta = input("Digite 'S' para continuar: ").upper()

busca=input("Digite o nome do equipamento que deseja saber o valor: ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("O Valor do item '",equipamentos[indice],"' é..: ", valores[indice])
    # print("Serial.:", seriais[indice])


serial=int(input("Digite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
  if seriais[indice]==serial: # Todo o equipamento que será excluido
    del departamentos[indice]
    del equipamentos[indice]
    del seriais[indice]
    del valores[indice]
    break

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

# funções para listas numéricas
# valores=[]
# for elemento in inventario:
#   valores.append(elemento[1])
# if len(valores)>0:
#   print("O equipamento mais caro custa: ", max(valores))
#   print("O equipamento mais barato custa: ", min(valores))
#   print("O total de equipamentos é de: ", sum(valores))

# ESTRUTURA DE UMA FUNÇÃO
# def <identificador da funcao> (<parametro(s)>):
# 	<código que será executado>
# 	return <Dado que será retornado, caso seja necessário>