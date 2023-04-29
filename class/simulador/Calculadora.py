"""
    Sobrecarga de Métodos

    Com essas funções definidas podemos personalizar a forma do seu comportamento,
    assim ocomo seu retorno.

__add__(self, other) : Sobrecarga do operador de adição (+)
__sub__(self, other) : Sobrecarga do operador de subtração (-)
__mul__(self, other) : Sobrecarga do operador de multiplicação (*)
__truediv__(self, other) : Sobrecarga do operador de divisão (/)
__floordiv__(self, other) : Sobrecarga do operador de divisão de piso (//)
__mod__(self, other) : Sobrecarga do operador de módulo (%)
__pow__(self, other[, modulo]) : Sobrecarga do operador de potência (**)
__and__(self, other) : Sobrecarga do operador "e" bit a bit (&)
__or__(self, other) : Sobrecarga do operador "ou" bit a bit (|)
__xor__(self, other) : Sobrecarga do operador "ou exclusivo" bit a bit (^)
__lshift__(self, other) : Sobrecarga do operador de deslocamento à esquerda (<<)
__rshift__(self, other) : Sobrecarga do operador de deslocamento à direita (>>)
__neg__(self) : Sobrecarga do operador unário de negação (-)
__pos__(self) : Sobrecarga do operador unário de positivo (+)
__abs__(self) : Sobrecarga do operador unário de valor absoluto (abs())
__invert__(self) : Sobrecarga do operador unário de inversão bit a bit (~)
__eq__(self, other) : Sobrecarga do operador de igualdade (==)
__ne__(self, other) : Sobrecarga do operador de diferença (!=)
__lt__(self, other) : Sobrecarga do operador "menor que" (<)
__le__(self, other) : Sobrecarga do operador "menor ou igual a" (<=)
__gt__(self, other) : Sobrecarga do operador "maior que" (>)
__ge__(self, other) : Sobrecarga do operador "maior ou igual a" (>=)
__len__(self) : Sobrecarga do operador de comprimento (len())
__getitem__(self, key) : Sobrecarga do operador de indexação (x[i])
__setitem__(self, key, value) : Sobrecarga do operador de atribuição de indexação (x[i] = value)
__iter__(self) : Sobrecarga do operador de iteração (for x in iterable:)
__next__(self) : Sobrecarga do operador de iteração (next(iterable))
__call__(self[, args...]) : Sobrecarga do operador de chamada de função (x(args))

"""
import bancos

class Calculadora:


    def __add__(self,other):
        print(f'Poderia concatenar uma string {self.cor} e {other.cor}')
        return (str(f'{self.cor} e {other.cor}'))
