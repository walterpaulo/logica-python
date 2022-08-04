import json

f = open("clientes.json","w")
clientes = []
cliente = {
  "id": 1,
  "nome": "walter",
  'email': "walter@hotmail.com"
}
clientes.append(cliente)
try:
  cliente_json = json.dumps(clientes)
  f.write(cliente_json)
except Exception as e:
  print(e)
  print("Algo deu errado na escrita do arquivo")
finally:
    f.close()