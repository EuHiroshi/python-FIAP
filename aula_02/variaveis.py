# # nome = "Humberto Delgado"
# # empresa = 'Fiap'
# # qtde_funcionarios = 500
# # mediaMensalidade = 856.50

# nome = input("Digite um funcionario: ")
# empresa = input('Digite a instituição: ')
# qtde_funcionarios = int(input("Digite a quantidade de funcionários: "))
# mediaMensalidade = float(input("Digite a média da mensalidade: "))

# print(nome + " trabalha na empresa " +
#       empresa)  # "+" representa concatenação/junção de strings
# print(
#   "Possui: ", qtde_funcionarios, " funcionários."
# )  # "," representa a separação do primeiro texto, a variável e o segundo texto
# print(
#   "A média da mensalidade é de: " + str(mediaMensalidade)
# )  # convertemos o float para string, para que o python nao tente realizar uma operação matemática
# print("=== Verifique os tipos de dado da variável [nome] é: ", type(nome))
# print("=== Verifique os tipos de dado da variável [empresa] é: ", type(empresa))
# print("=== Verifique os tipos de dado da variável [qtde_funcionarios] é: ", type(qtde_funcionarios))
# print("=== Verifique os tipos de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))
# "=" representa atribuição, "==" representa comparação
# "and" representa E, "or" representa ou

# ========================================================
#  IF ELIF ELSE
# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# if idade >= 65:
#   print("O paciente " + nome + " POSSUI atendimento prioritário")
# elif idade < 18:
#   print("O paciente " + nome + " Deve ser encaminhado para outro setor")
# else: 
#   print("O paciente " + nome + " NÃO possui atendimento prioritário")

# ========================================================
# WHILE FOR
# numero = int(input("digite um numero: "))
# while numero < 100 :
#     print(" " + str(numero))
#     numero = numero + 1
# print("Laço encerrado")

numero = int(input("até que numero devemos contar: "))
for i in range(1, (numero + 1)): # range(start, stop, step)
  print(" " + str(i))