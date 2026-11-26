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

print("Seja bem vinda mikaelly ao seu sistema pessoal de economia!")
print("Vamos economizar R$1050 para o show do BTS\n")

valor = GetValue(0, None, float, "Insira a quantidade de suas economias: ")

if valor >= 1050:
  print("Parabéns!, você atingiu o valor necessário para o show")
  print(f"Sua família lhe enviou R$100 extras para lembrancinhas, valor final R${valor + 100}")
else:
  print("Infelizmente o valor guardado não é o suficiente, junte para um próximo show")