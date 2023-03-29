# Função para adição
def add(x, y):
   return x + y

# Função para subtração
def subtract(x, y):
   return x - y

# Função para multiplicação
def multiply(x, y):
   return x * y

# Função para divisão
def divide(x, y):
   return x / y

# Menu de opções
print("Selecione uma operação.")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Obter entrada do usuário
escolha = input("Digite sua escolha (1/2/3/4): ")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if escolha == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif escolha == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif escolha == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif escolha == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Opção inválida")
