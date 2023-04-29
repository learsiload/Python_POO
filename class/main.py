from produtos.Casa import Casa
from bancos.Bradesco import Bradesco
from bancos.CaixaEconomica import CaixaEconomica
from bancos.Itau import Itau
from bancos.Nubank import Nubank
from bancos.Sicoob import Sicoob

"""
    Fontes: 
        https://www.youtube.com/watch?v=t46MCgpBU90&t=4s&ab_channel=pythonando
"""

#### HERANÇA

cliente1 = Bradesco('Preta',240,15,'Nova America',6)
cliente1.__dict__

cliente1.financiar()
cliente1.__dict__

cliente1.avaliarCasa(0)
cliente1.__dict__

cliente1.condicaoCasa(0)
cliente1.__dict__

#### POLIMORFISMO

cliente2 = Itau('Verde',210,21,'Rua Tira Dentes',5)
cliente2.__dict__

cliente2.condicaoCasa(0,0)
cliente2.__dict__


#### ENCAPSULAMENTO
from bancos.Sicoob import Sicoob

cliente3 = Sicoob('Rosa',280,45,'Av. Ciquentenário',3)
# essa função __dict__ consegue mostrar o valor nas variáveis ocultas.
cliente3.__dict__

# Não é permitido acesse os atributos diretamente assim.
cliente3.financiar(4)
cliente3.financiar(3.5)

cliente3.valorComDesconto
cliente3._valorComDesconto

cliente3.valorComDesconto = '15'
cliente3._valorComDesconto = '15'


#### SOBRECARGA DE OPERADORES
from simulador.Calculadora import Calculadora

conta1 = Calculadora()
conta2 = Calculadora()
conta1.cor = 'Azulão'
conta2.cor = 'Amarelão'

conta1 + conta2