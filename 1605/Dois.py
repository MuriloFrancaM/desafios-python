numeros = []

for i in range (5):
    num = int(input(f'digite o {i+1}º número:'))
    numeros.append(num)
    
soma = sum(numeros)
print(f'A soma dos números é {soma}')