def GetValue(min, max, v_type, text):
    while True:
        try:
            value = v_type(input(text))
    
        except ValueError:
            print("Digite um valor válido.")
            continue

        if not min == None and not max == None: 
          if not min <= value <= max:
                print(f"Digite uma valor entre {min} e {max}")
                continue
        elif max == None and not min == None: 
          if value < min:
                print(f"Digite uma valor maior ou igual a {min}")
                continue
        elif min == None and not max == None: 
          if value > max:
                print(f"Digite uma valor menor ou igual a {max}")
                continue
        
        return value

print("Bem vindas Kauane e Kauanya a loja de materiais educativos!")
print("Leve 2 livros ou 3 jogos para obter desconto especial\n")

livros = GetValue(0, None, int, "Insira a quantidade de livros comprados: ")
jogos = GetValue(0, None, int, "Insira a qunatidade de jogos comprados: ")
valor = GetValue(0, None, float, "Insira o valor da compra: ")

if jogos >= 3 or livros >= 2 and valor > 25:
  valor -= 25
  print("\nDesconto de R$25,00 aplicado!")
else:
  print("\nCompre mais jogos e livros para obter desconto especial")

print(f"Valor final: R${valor:.2f}")