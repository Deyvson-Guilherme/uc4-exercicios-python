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

print("Bem vinda Marli, Vamos checar suas atividades!\n")

atividade = GetValue(0, None, int, "Insira a quantidade de atividades entreges: ")
nota = GetValue(0, 10, float, "Insira a sua nota inicial: ")

if nota >= 7 and atividade >= 5:
  print("Parabéns, você cumpriu os requesitos, com isso receberá 2 pontos extras")
else:
  print(f"Sua nota final será {nota}, entregue pelo menos 5 atividades e tenha \nnotal igual a 7 para obter pontos extras na próxima")