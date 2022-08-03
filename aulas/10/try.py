# try:
#   print(x)
# except:
#   print("Error...")

try:
  x = "r1"
  print(int(x))
except:
  print(f"O {x} não é número")


# Tipo de erro
try:
  x = "r1"
  print(int(x))
except NameError:
  print(f"O {x} não é número")
except:
  print("erro 2")

# retorna erro para false ou true
try:
  print(x)
except:
  print("Error...")
else:
  print("deu certo")

# Sempre cai no finally, independente de erro
try:
  print(x)
except:
  print("Error...")
finally:
  print("deu certo")


# dentro de um try, abre, escreve e fecha arquivo
try:
  f = open("demofile.txt")
  try:
    # w = escrita
    # r = leitura
    f.write("lorum ...", "w")
  except:
    print("Error...")
  finally:
    f.close()
except:
  print("erro")


# retorna erro
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below")


# retorna erro personalizado
x = "oi"
if not type(x) in int:
  raise Exception("number")



