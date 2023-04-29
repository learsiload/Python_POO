# ENCAPSULAMENTO -----------------------------------
# » quarto pilar

# Métodos acessores e modificadores

from produtos.Casa import Casa

class Sicoob(Casa):

    def __init__(self, cor, tamanho, numero, rua, qtComodos):
        super().__init__(cor, tamanho, numero, rua, qtComodos)

        

    
    # Função para aplicar um desconto sobre o valor que seria pago sob o tamanho do terreno
    # Diferencial desse banco

    @property
    def valorComDesconto(self):
        return self.__valorComDesconto

    @valorComDesconto.setter
    def valorComDesconto(self,valor):
        if not isinstance(valor,(float,int)):
            raise ValueError('Não permitido atribuir esse valor')
        self.__valorComDesconto = valor        
        print(f'Caro cliente, nossa agência irá conceder um desconto de {self.__valorComDesconto} %')


    """
        (get & set)
        Essa função financiar, utiliza um parâmtro valorComDesconto que só pode ser
        acessado se antes passar pela @valorComDesconte.setter que pose ser usadao 
        apenas para atribuir o valor ou para validar ou para efetuar um cálculo.
        [técina do emcapsulamento]
    """
    def financiar(self,valor):
        self.financiamento = 'Financiada Pelo Sicoob'
        self.valorComDesconto = valor
        self.valorFinanciado = (valor/100) * self.tamanho
        print(f'O valor com desconto será de {self.valorFinanciado}')
    pass
