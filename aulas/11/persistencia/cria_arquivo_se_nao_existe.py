from os.path import exists


file_exists = exists("clientes.json")


try:
  if not file_exists:
    open("clientes.json","w")
  f = open("clientes.json","w")
except Exception as e:
  print(e)
  print("Algo deu errado na escrita do arquivo")
finally:
    f.close()