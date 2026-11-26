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
  
print("Bem vindo ao sistema de agendamento de Milena!")
print("Taxa extra em distâncias superiores a 10km\n")
  
nome = input("Insira deu nome: ")
distancia = GetValue(0, None, float, "Insira a distância em KM da sua casa até Milena: ")

valor = 180
entrega = 25 if distancia > 10 else 0
total = valor + entrega

print("\nNota de pagamento:")
print(f"Cliente: {nome}")
print(f"Valor do serviço: R${valor:.2f}")
print(f"Taxa de desloamento: R${entrega:.2f}")
print(f"Valor total R${total:.2f}")