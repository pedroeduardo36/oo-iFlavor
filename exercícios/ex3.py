from datetime import date


class Pessoa: 
    def __init__(self, nome='', idade=0, profissao=''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'O nome é: {self._nome}. Tem {self._idade} anos de idade, sua profissão é {self._profissao}'

    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Sou {self._profissao}, e tenho {self._idade} anos de idade' 
        else:
            return f'Olá, sou {self._nome}'
        
    def aniversao(self):
        self._idade += 1
    


pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

pessoa1.aniversao()
pessoa3.aniversao()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()


print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
