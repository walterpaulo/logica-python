## Dia 16 - 09/08/2022[  🔙](../../README.md)

- Conexão com banco de dados;
  - caso for usar o Mysql, evitar nomear o arquivo de mysql. Ocorre erro durante o processo.
- Instalação do Env para o Python [init.py](../15/init.py);
- Adicionado variável de ambiente, [aquivo modelo](start.sh) para exportar variáveis;
  - Captura de variável de ambiente
    - os.getenv("HOST")
    - os.getenv("DATABASE")
    - os.getenv("USER")
    - os.getenv("PASSWORD")
- Extra, conectar em banco Postgreql, [exemplo](./postgresql/init.py)
- Conectar em banco Mongo, [exemplo](./mongo/init.py)

- Consulta do primeiro registro no db
```
...
cursor = connection.cursor()
cursor.execute("select * from usuarios")

# retorna uma lista de tuple
records = cursor.fetchall()

print(records[0])

# Retorna os itens na tela
for record in records:
  print(f"id: {record[0]})
  print(f"nome: {record[1]})
  print(f"endereço: {record[2]})
...
```

