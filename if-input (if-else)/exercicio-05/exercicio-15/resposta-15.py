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

print("Bem vindo ao Senac\n")

print("Este computador não está se comportando devidamente. um atualização é necessária")  
estado = GetValue(0, 1, int, "Você está usando ele agora? (0 = não  1 = sim): ")

if estado == 1:
    print("\nOk, termine suas atividades, atualizaremos mais tarde!")
elif not estado == 1:
     print("\nComputador disponível! Atualização autorizada.")