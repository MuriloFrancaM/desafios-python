numeros = []

for i in range(6):
    num = int(input(f'Digite o {i+1}º número: '))
    numeros.append(num)

print('Números pares digitados:')
for numero in numeros:
    if numero % 2 == 0:
        print(numero)