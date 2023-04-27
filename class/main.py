from produtos.Casa import Casa
from bancos.Bradesco import Bradesco
from bancos.CaixaEconomica import CaixaEconomica
from bancos.Itau import Itau
from bancos.Nubank import Nubank


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
cliente3 = Nubank('Rosa',280,45,'Av. Ciquentenário',3)
# essa função __dict__ consegue mostrar o valor nas variáveis ocultas.
cliente3.__dict__

# Não é permitido acesse os atributos diretamente assim.
cliente3.__bonus
cliente3.__taxaFinanciamento

cliente3.aplicarDesconto(5)

