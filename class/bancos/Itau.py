# POLIMORFISMO ---------------------------------------------
# » terceiro pilar

"""
    Com essa funcionalidade uma classe filha, pode alterar o valor
    de um método da classe pai mesmo já definido.
"""

from produtos.Casa import Casa

class Itau(Casa):
    def __init__(self, cor, tamanho, numero, rua, qtComodos):
        super().__init__(cor, tamanho, numero, rua, qtComodos)
    
    def financiar(self):
        self.financiamento = 'Financiada Pelo Itaú'    

    """
        Pq usar o polimorfismo:
        Imagine que o banco Itaú possue sua própria forma de avaliação da casa para o financiomento
        avaliarCasa o Itaú faz igual aos demais bancos, já
        condicaoCasa é um pouco diferente, dessa forma nós mudanmos alguma coisa de um método já existente
        e herdado, refazendo-o
    """ 

    # Neste caso o método trás as opções e os textos já definidos, vc só passa o parâmetro.
    def avaliarCasa(self, avaliacao):
        print('Método Padrão')
        return super().avaliarCasa(avaliacao)
    
    # Neste caso o Itaú preciou mudar uma regra dessa função
    def condicaoCasa(self, condicao:bool,regraItau:bool):
        print('Método Itaú')
        super().condicaoCasa(condicao)
        a, b = 'O Engeneiro vai assinar','Vamos enviar o Contrutor para Corrigir'
        self.regraItau =  a if regraItau == 1 else b
        return 'Método do Itaú'
    

# financiamento3 = Itau('Cinza','189',766,'Rua Potiraguá',3)
# financiamento3.__dict__
# financiamento3.avaliarCasa(1)
# financiamento3.__dict__ 

# # Agora chamando a classe modificada
# financiamento3.condicaoCasa(1,1)
# financiamento3.__dict__ 