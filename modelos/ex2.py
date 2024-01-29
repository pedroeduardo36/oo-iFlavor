class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = int(duracao)
        Musica.musicas.append(self)
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica('Isnt she lovely', 'Stevie Wonder', 230)
musica2 = Musica('Leao', 'Elevation Worship', 230)

Musica.listar_musicas()

#ex2
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)

carro1 = Carro('Onix Lt', 'Branco', 2014)
carro2 = Carro('Audi A3', 'Branco', 2000)