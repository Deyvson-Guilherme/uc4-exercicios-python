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
  
print("Bem vindo a checagem de média!")
print("Esfihas grátis para a sale com média >= 8\n")
  
sala = GetValue(0, None, int, "Insira a quantidade de alunos na sala: ")
media = GetValue(0, sala, int, "Insira a quantidade de alunos com média >= 8: ")

if media == sala:
    print("\nEsfihas grátis para todos os alunos!")
    print("Preço da Esfiha: R$8,00")
    print(f"Total de esfihas compradas para toda a sala: R${(sala * 8):.2f}")
else:
     print("\nNem todo mundo atingiu a meta, as esfihas ficam para a próxima")