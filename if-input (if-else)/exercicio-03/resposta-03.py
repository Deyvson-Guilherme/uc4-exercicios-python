def GetValue(min, v_type, text):
    while True:
        try:
            value = v_type(input(text))
    
        except ValueError:
            print("Digite um valor válido.")
            continue
        
        if not min == None: 
            if value <= min:
                print(f"Digite uma valor maior que {min}")
                continue
        
        return value

print("Bem vindo a loja de jogos da Nitendo")
print("Comprando pelo menos 3 jogos e gastando acima de R$500 você receberá pontos extras!")
print("Se identifique: \n")

nome = input("Insira seu nome: ")
pontos = GetValue(0, int, "Insira seu total de pontos atual: ")
quantidade = GetValue(0, int, "Insira a quantidade de jogos escolhida: ")
valor = GetValue(0, float, "Insira o valor total da compra: ")

print(f"\nBom dia {nome}, você está levando {quantidade} jogos num valor total de R${valor}")

if valor > 500:
  print(f"Você cumpriu as exigência do benefício!, um total de 200 pontos será adicionado a sua atual quantidade de {pontos} pontos\n")
  pontos += 200
else:
  print(f"Você não concorrerá ao benefício de pontos dessa vez\n")

print(f"Status:")
print(f"Cliente: {nome}")
print(f"Jogos comprados: {quantidade}")
print(f"Valor da compra: {valor}")
print(f"Pontos: {pontos}")