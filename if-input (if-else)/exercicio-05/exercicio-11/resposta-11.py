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
  
print("Bem vindas Isabela a plataforma de engajamento de publicações!")
print("Obtenha 100 curtidas ou 30 comentários para conseguir pontos de engajamentos\n")
  
curtidas = GetValue(0, None, int, "Insira a quantidade de curtidas: ")
comentarios = GetValue(0, None, int, "Insira a qunatidade de comentarios: ")
  
if curtidas >= 100 and comentarios >= 30:
  print("\nParbéns, meta atingida, você ganhou 50 pontos extra de engajamento!")
else:
  print("\nAtinja a meta na próxima para obter pontos de engajamento")