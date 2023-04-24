# HERANÇA---------------------------------------------
# » segundo pilar

from produtos.Casa import Casa

class Bradesco(Casa):
    """
        Classe também herdando casa, mas agora invocando um método
        built-in super que reaproveita os parâmetros da classe PAI,
        e você ainda pode adicionar um outro parâmetro específico.
    """
    def __init__(self, cor, tamanho, numero, rua, qtComodos):
        super().__init__(cor, tamanho, numero, rua, qtComodos)
    
    def financiar(self):
        self.financiamento = 'Financiada Pelo Bradesco'




# financiamento2 = Bradesco('Amarela','180','96','Av Getúlio',4)
# # Abstrai os valores padrões da classe
# financiamento2.__dict__

# # Utilizando o método herdado da Classe Pai | Abaixo vamos usar o porlimorfismo dessa classe
# financiamento2.condicaoCasa(1)
# financiamento2.__dict__

# # atribui mais um parâmtro através da nova função específica dessa classe Bradesco
# financiamento2.financiar()
# financiamento2.__dict__



