altura = float (input("Digite sua altura:"))
peso = float (input("Digite seu peso:"))
imc = peso / (altura ** 2)
if imc<=18.5:
    print ('Você está abaixo do peso')
elif imc >=18.5 and imc <= 24.9:
    print ('Você está no peso ideal')
elif imc >=25 and imc <= 29.9:
    print ('Você está sobrepeso')
else:
    print('Você está obeso')