def mostra(numero = ""):
  return f"::Mostrando uma informão na tela {numero}"

while True:
  print("=== Bem vindo ao programa ===\n")
  print("Digite um opção:\n")
  print("1 - Mostrar algo na tela mais 1")
  print("2 - Mostrar algo na tela mais 2")
  print("3 - Mostrar algo na tela mais 3")
  print("4 - Mostrar algo na tela mais 4")
  print("5 - Mostrar algo na tela mais 5")
  print("10 - Sair do programa")

  opcao = int(input())

  if opcao == 10:
    break
  elif opcao == 1:
    print("{mostra()}")
  elif opcao == 2:
    print(f"{mostra(2)} - {2}")
  elif opcao == 3:
    print(f"{mostra(3)} - {3}")
  elif opcao == 4:
    print(f"{mostra(4)} - {4}")
  elif opcao == 5:
    print(f"{mostra(5)} - {5}")
  