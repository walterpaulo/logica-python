import psycopg2
import os

# export DATABASE_PASSWORD
# export DATABASE_IP
# export DATABASE_USER

conexao = psycopg2.connect(host=os.getenv("DATABASE_IP"), database='meuteste',
user=os.getenv("DATABASE_USER"), password=os.getenv("DATABASE_PASSWORD"))
cursor = conexao.cursor()
sql = 'create table cidade (id serial primary key, nome varchar(100), uf varchar(2))'
cursor.execute(sql)
sql = "insert into cidade values (default,'Goiânia','GO')"
cursor.execute(sql)
conexao.commit()
cursor.execute('select * from cidade')
# (1, 'Goiânia', 'GO')
recset = cursor.fetchall()
for rec in recset:
  print(rec)
conexao.close()