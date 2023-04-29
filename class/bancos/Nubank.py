# ENCAPSULAMENTO -----------------------------------
# » quarto pilar

"""
    Quer dizer sobre os privilégios dos acessos, como em java (public e private), ou seja,
    public quando pode ser acessado e alterado
    private quando não pode ser acessado diretamente ou alterado.
"""

from produtos.Casa import Casa

class Nubank(Casa):
    
    # Poderia usa-se também 1 underline, e o atributo seria fracamente privado
    # Esse seria um atributo fortimente private por causa dos dois underline antes do nome
    __bonus = 2

    def __init__(self, cor, tamanho, numero, rua, qtComodos):
        # Exemplo de outro atributo private
        self.__taxaFinanciamento = 0.8
        super().__init__(cor, tamanho, numero, rua, qtComodos)


# financiamento4 = Nubank('Amarela',220,68,'Rua Grande Otelo',3)
# financiamento4.__dict__

# # Veja que não se pode acessar esses atributos
# financiamento4.__taxaFinanciamento
# financiamento4.__bonus
# """
#     PORÉM, se fosse o caso, um hacker poderia acessar e modificar esses valores utilizando _ underline antes
#     do nome da classe. QUE SERIA UM PERIGO.
#     Então pense bem ao utilizar o ENCAPSULAMENTO EM PYTHON
# """
# financiamento4._Nubank__taxaFinanciamento


# based: https://www.youtube.com/watch?v=yZ83sZUvLVw&t=366s&ab_channel=ByLearn