class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        print(f"{'Nomde do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Estado")
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo ✅' if self._ativo else 'Desativo ❌'



restaurante_massa = Restaurante('Massa', 'Italiano')

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Fast food')

Restaurante.listar_restaurantes()

