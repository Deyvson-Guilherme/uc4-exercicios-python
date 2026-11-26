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
  
print("Bem vindo ao desaio de exploração do senac!")
print("Pontos extras para quem visitar ao menos 4 laboratórios\n")
  
labs = GetValue(0, None, int, "Insira a quantidade de laboratórios que visitou: ")
extra = 20 if labs >= 4 else 0
pontos = (labs * 10) + extra

print("\nStatus da exploração:")
print(f"Total de labs visitados: {labs}")
print(f"Pontos extras: {extra}")
print(f"Pontuação final: {pontos}")