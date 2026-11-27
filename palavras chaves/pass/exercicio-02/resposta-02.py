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


class ServiçoCliente():
  def cadastrar(self):
    pass

  def listar(self):
    pass

  def remover(self):
    pass

print("Bem vindo ao launcher da API de gerência!")
input("Pressione Enter tecla iniciar...\n")

api = ServiçoCliente()
print("Api de seviço de cliente inicializada!")

print("1. Cadastrar\n2. Listar\n3. Remover\n")
acao = GetValue(1, 3, int, "Insira o número da ação que deseja: \n")

if acao == 1:
  api.cadastrar()
  print("Cadastro feito com sucesso!")
elif acao == 2:
  api.listar()
  print("Listagem feita com sucesso!")
elif acao == 3:
  api.remover()
  print("remoção feita com sucesso!")