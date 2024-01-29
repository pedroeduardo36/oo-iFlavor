class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_massa = Restaurante('Massa', 'Italiano')

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Fast food')

restaurantes = [restaurante_massa, restaurante_praca, restaurante_pizza]

print(vars(restaurante_pizza))
print(vars(restaurante_praca))
print(vars(restaurante_massa))

