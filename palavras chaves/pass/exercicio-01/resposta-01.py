import os
import time

os.system("cls")

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
        time.sleep(2)
        os.system("cls")
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

def cadastrar():
  pass

def listar():
  pass

def remover():
  pass

print("Bem vindo ao sistema de gerência!")
print("Aqui estão as funcionalidades:\n")

print("1. Cadastrar\n2. Listar\n3. Remover\n")

acao = GetValue(1, 3, int, "Insira o número da ação que deseja: ")

if acao == 1:
  cadastrar()
  print("Cadastro feito com sucesso!")
elif acao == 2:
  listar()
  print("Listagem feita com sucesso!")
elif acao == 3:
  remover()
  print("remoção feita com sucesso!")