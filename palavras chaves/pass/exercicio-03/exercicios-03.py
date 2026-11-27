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

def logar_nome():
  input("Insira seu nome: ")
  pass
  
def logar_senha():
  input("Insira sua senha: ")
  pass
  
def cadastrar_nome():
  input("Cadastre seu nome: ")
  pass
  
def cadastrar_senha():
  input("Cadastre sua senha: ")
  pass

print("bem vindo ao torrent filmes!")
print("Prossiga para o login")

while True:
  print("\nAções:\n1. logar\n2. cadastrar\n")
  acao = GetValue(1, 2, int, "Insira o digito da ação desejada: ")

  if acao == 2:
    print("=" * 90)
    cadastrar_nome()
    cadastrar_senha()
    print("\nVocê se cadastrou no torrent filmes!")
    print("=" * 90)
  
  elif acao == 1:
    print("=" * 90)
    logar_nome()
    logar_senha()
    print("\nVocê logou no torrent filmes!")
    print("=" * 90)
    break