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

incrementacoes = 0

print("Bem vindos Valquíria, Michele e Rhalldney, organizar a palestra!\n")

convidados = GetValue(0, None, int, "Insira a quantidade de participantes: ")
cadeiras = GetValue(0 , None, int, "Insira a qunatidade de cadeiras: ")


falta = True if convidados >= 80 and cadeiras < convidados else False

while falta:
  incrementacoes += 1
  cadeiras += 30
  falta = True if convidados >= 80 and cadeiras < convidados else False

if incrementacoes == 0 and convidados <= cadeiras:
  print(f"{convidados} convidade e {cadeiras} cadeiras, todos visitantes acomodados")
elif incrementacoes == 0 and convidados > cadeiras:
  print(f"{convidados} convidade e {cadeiras} cadeiras")
  print(f"{convidados - cadeiras} convidados estão sem cadeiras, mas só podemos encomedar mais cadeiras quando atingirmos 80 convidados")
elif incrementacoes > 0:
  print(f"{convidados} convidade e {cadeiras} cadeiras")
  print(f"Foram feitos {incrementacoes} pedidos de 30 cadeiras")