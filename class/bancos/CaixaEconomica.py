# HERANÇA---------------------------------------------
# » segundo pilar

from produtos.Casa import Casa

class CaixaEconomica(Casa):
    """
       A Classe CaixaEconomica herança a classe Casa e seus atributos
       e método, ao chamar o método __init__ o construtor é invocado.
       Porém, algumas propriedades já são definidas diretamente, por serem
       particularidade da nova classe.
    """
    def __init__ (self,cor,numero,rua):
        self.cor = cor
        self.tamanho = 200
        self.numero = numero
        self.rua = rua
        self.qtComodos = 4

    def financiar(self):
        self.financiamento = 'Financiada Pela Caixa'


"""
    Ao criar um classe que herda outras você recriar os parâmetros,
    e/ou pode adicionar novos parâmentros
    MAS precisar passar os nomes.
"""
financiamento1 = CaixaEconomica('azul','54','Jequié')
financiamento1.__dict__

financiamento1.financiar()
financiamento1.__dict__