numeros = []

for i in range (5):
    num = int(input(f'Digite os números: '))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')