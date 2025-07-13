# 1) Solicita ao usuário que digite seu nome

nome = input("Qual seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario = float(input("Qual o seu salario: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus = float(input("Qual o percentual do seu bonus: "))

bonus = bonus / 100

# 4) Calcule o valor do bônus final

comissao = salario * bonus

# 5) Imprima cálculo do KPI para o usuário

#print(comissao)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

#print("Olá ", nome , ", Voce tem um salario de", salario, ". E voce recebera um bonus de ", comissao)

print(f"Olá {nome}, voce tem um salario de {salario}, e voce recebera um bonus de {comissao}")
      
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?



