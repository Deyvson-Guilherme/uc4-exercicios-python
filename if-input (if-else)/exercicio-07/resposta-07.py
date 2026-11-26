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

print("Seja bem vinda Wandercyra a plataforma de pagamentos musicais\n")

musica = input("Insira o nome da sua música: ")
views = GetValue(0, None, int, f"Quantas visualizações {musica} teve: ")
likes = GetValue(0, None, int, f"Quantas curtidas {musica} teve: ")

if views > 1000 or likes > 200:
  print(f"Parabéns, você receberá um saldo de R$150 pela música {musica}")
else:
  print(f"As condições não foram atingindas, obtenha 1000 visulizações ou 200 curtidas em {musica}")