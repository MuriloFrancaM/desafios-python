preco = float (input("Digite o preço do produto:"))
desconto = float (input('Digite o percentual do desconto:'))
valordesconto = float ((desconto * preco) / 100)
precofinal = float (preco - valordesconto)

print(f'Desconto de {valordesconto:.2f}. Novo preço:{precofinal:.2f}')