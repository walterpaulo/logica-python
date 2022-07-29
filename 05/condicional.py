# print("Digite seu nome:")
# nome = input()

# if nome == "luciano":
#   numero = int(input("Opa Lucino, digite um número"))
#   if numero == 20:
#     print("Achou")
#   else:
#     print("Errou")
  

numero = int(input("Digite o tipo:\n1 - Número\n2- String\n"))
resultado = "Número" if numero == 1 else 'String'
print(f"O tipo digitado foi {resultado}")