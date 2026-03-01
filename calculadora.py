print("Olá! Seja bem vindo! Espero que essa calculadora lhe seja útil :)")
while True:
  print()
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  print("5. Sair")
  escolha = input("Escolha uma opção (1-5):")
  print()
  if escolha == "1":
    num1 = float(input("Digite o primeiro número:").replace(",", "."))
    num2 = float(input("Digite o segundo número:").replace(",", "."))
    resultado = num1 + num2
    print()
    print(f"O resultado da soma é {int(resultado) if resultado.is_integer() else resultado}")
  elif escolha == "2":
    num1 = float(input("Digite o primeiro número:").replace(",", "."))
    num2 = float(input("Digite o segundo número:").replace(",", "."))
    resultado = num1 - num2
    print()
    print(f"O resultado da subtração é {int(resultado) if resultado.is_integer() else resultado}")
  elif escolha == "3":
    num1 = float(input("Digite o primeiro número:").replace(",", "."))
    num2 = float(input("Digite o segundo número:").replace(",", "."))
    resultado = num1 * num2
    print()
    print(f"O resultado da multiplicação é {int(resultado) if resultado.is_integer() else resultado}")
  elif escolha == "4":
    num1 = float(input("Digite o primeiro número:").replace(",", "."))
    num2 = float(input("Digite o segundo número:").replace(",", "."))
    resultado = num1 / num2
    resto = num1 % num2
    print()
    print(f"O resultado da divisão é {int(resultado) if resultado.is_integer() else resultado} com resto {int(resto) if resto.is_integer() else resto}")
  elif escolha == "5":
    print("Obrigado por usar a calculadora! Até a próxima!")
    break
  else:
    print("Opção inválida. Tente novamente.")

