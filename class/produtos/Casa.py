# CLASSE ---------------------------------------------
# » priemeiro pilar
class Casa:
    """
        Método contrutor para os objetos do tipo casa
        Contém por default, exemplo os elementos que compoem uma casa
        ou que indentifique uma casa
    """
    def __init__(self,cor,tamanho,numero,rua,qtComodos):
        self.cor = cor
        self.tamanho = tamanho
        self.numero = numero
        self.rua = rua
        self.qtComodos = qtComodos
        self.status = 'Projeto na Planta'

    """
        Métodos de ação ou de configuração
        O parâmetro self, instância o objeto criado pelo construtor a atribui
        os outros parâmetros adicionados pelos métodos: ex: status do método construir.
    """
    def condicaoCasa(self, condicao:bool): # 1 = Casa Nova | 0 Casa Reformada
        a , b = "A casa é Nova", "A casa é Reformada"
        self.condicao = a if condicao == 1 else b
        return 1 if condicao == 1 else 0
   

    def avaliarCasa(self,avaliacao:bool):# 1 = Casa OK | 0 = casa deve ser adaptada
        n , u = "A casa segue os padrões", "A casa deve ser adaptada"
        self.avaliacao = n if avaliacao == 1 else u
        return 1 if avaliacao == 1 else 0

# # Passando os atrubutos para o objeto criado chamado kz1   
# kz1 = Casa('Azul',420.2,1800,'Rua da Galaxia',6)
# # Exibi todos os atributos da instância
# kz1.__dict__
# """
# {'cor': 'Azul',
#  'tamanho': 420.2,
#  'numero': 1800,
#  'rua': 'Rua da Galaxia',
#  'qtComodos': 6,
#  'status': 'Projeto na Planta'}
# """
# # Chamando o método contruir
# kz1.construir()
# # Agora esse objeto possui um novo parâmtro
# kz1.__dict__
# """
# {'cor': 'Azul',
#  'tamanho': 420.2,
#  'numero': 1800,
#  'rua': 'Rua da Galaxia',
#  'qtComodos': 6,
#  'status': 'Casa Construida'}
# """