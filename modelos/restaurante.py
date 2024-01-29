class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_massa = Restaurante()
restaurante_massa.nome = 'Massa'
restaurante_massa.categoria = 'Gourmet'

restaurante_prata = Restaurante()
restaurante_prata.nome = 'Massa'
restaurante_prata.categoria = 'Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

restaurantes = [restaurante_massa, restaurante_pizza, restaurante_prata]

if restaurante_pizza.ativo:
    print('O restaurante está ativo')
else:
    print('O restaurante está desativado')

categoria = Restaurante.categoria
restaurante_prata.nome = 'Bistrô'

print(vars(restaurante_pizza))