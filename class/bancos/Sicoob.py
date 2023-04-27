# ENCAPSULAMENTO -----------------------------------
# » quarto pilar

from produtos.Casa import Casa

class Sicoob(Casa):

    def __init__(self, cor, tamanho, numero, rua, qtComodos):
        super().__init__(cor, tamanho, numero, rua, qtComodos)


        