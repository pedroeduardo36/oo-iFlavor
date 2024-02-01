class Musica:
    nome = ''
    artista = ''
    duracao = int #segundos

musica1 = Musica()
musica1.nome = 'Colossenses e suas linhas de amor'
musica1.artista = 'FHOP'
musica1.duracao = 360

musica2 = Musica()
musica2.nome = 'Diante de ti'
musica2.artista = 'Morada'
musica2.duracao = 283

musica3 = Musica()
musica3.nome = 'Os anjos te louvam'
musica3.artista = 'Eli Soares'
musica3.duracao = 520

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')