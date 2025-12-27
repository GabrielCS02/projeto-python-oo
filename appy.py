from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Lucas', 6)
restaurante_praca.receber_avaliacao('Adelvan', 5)
restaurante_praca.receber_avaliacao('Michel', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()