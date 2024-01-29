class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_prata = Restaurante()
restaurante_prata.nome = 'Prata'
restaurante_prata.categoria = 'Gourmet'

restaurante_varanda = Restaurante()

restaurantes = [restaurante_prata, restaurante_varanda]

print(vars(restaurante_prata))