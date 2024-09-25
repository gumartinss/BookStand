from modelos.avaliacao import Avaliacao

class Livro:
    livros = []
    

    def __init__(self, nome, categoria):
        self._nome =nome.title()
        self._categoria = categoria.upper()
        self._lido = False
        self._avaliacao = []
        Livro.livros.append(self)
        
    def __str__(self):
        return (f'{self._nome} | {self._categoria}')

    @classmethod
    def listar_livros(cls):
        #print(f'{'Nome do livro'.ljust(25)} | {('Categiria'.ljust(25))} | {'Avaliação'.ljust(25)} | {('Lido')}')
        for livro in cls.livros:
            print(f'{livro._nome.ljust(25)} | {livro._categoria.ljust(25)} | {str(livro.media_avaliacao).ljust(25)} | {livro.lido}')
            
    @property
    def lido(self):
        return '⌧' if self._lido else '☐'
    
    def alternar_estado(self):
        self._lido = not self._lido
        
    def receber_avaliacao(self, livro, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(livro, nota)
            self._avaliacao.append(avaliacao)
                
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media    