numero = 10
while numero > 0:
  if numero % 2 == 0:
    print(f"{numero} é um número par.")
  else:
    print(f"{numero} é um número ímpar.")
  numero -= 1

print("Numero ao final da execução:", numero)
