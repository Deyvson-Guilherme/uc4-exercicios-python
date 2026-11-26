def GetValue(min, text):
    while True:
        try:
            value = float(input(text))
    
        except ValueError:
            print("Digite um valor válido.")
            continue
        
        if not min == None: 
            if value <= min:
                print(f"Digite uma valor maior que {min}")
                continue
        
        return value

print("Bem vindo a loja do super soldado! Compras acimas de R$150 tem desconto especial\n")
valor = GetValue(0, "Insira o valor total da compra: ")


if valor > 150:
  print(f"Parabéns, desconto de R$30 aplicado, valor final {valor - 30}")
else:
  print(f"Valor final R${valor}, compre acima de R$150 para ter um desconto na próxima!")