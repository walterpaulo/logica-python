def chama_dados(index):
  if index == 10:
    return

  print("olá sou index: " + str(index))
  chama_dados(index + 1)

chama_dados(1)