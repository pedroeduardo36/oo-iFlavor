from modelos.restaurante import Restaurante
import os

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Pedro', 3)
restaurante_praca.receber_avaliacao('Jú', 4)
# restaurante_ravioli = Restaurante('Ravioli', 'Italiano')
# restaurante_outback = Restaurante('Outback', 'Australia')

def main():
    os.system('clear')
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()