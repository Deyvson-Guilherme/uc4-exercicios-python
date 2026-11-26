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

print("Bem vindo Anna Beatriz Giuliany a loja do super soldado!")
print("Vocês receberam um cartão de R$80, compras acima desse limite terão taxa adiconal de R$20")
valor = GetValue(0, "Insira o valor total da compra: ")


if valor > 80:
  print(f"\nLimite de R$80 ultrapassado! Valor final R${valor + 20}")
else:
  print(f"\nValor final R${valor}, Sem taxas adicionais")