numeros = []

for i in range (6):
    num = int (input(f'digite o {i+1}º número '))
    numeros.append(num)
    if num % 2 == 0:
        print(f'O número {num} é par')