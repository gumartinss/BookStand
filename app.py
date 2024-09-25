from modelos.livro import Livro
import os

livro_eragon = Livro('Eragon', 'Aventura')
livro_eragon.receber_avaliacao('Gustavo', 5)
livro_eragon.alternar_estado()

def main():
    Livro.listar_livros()
    
if __name__ == '__main__':
    main()

