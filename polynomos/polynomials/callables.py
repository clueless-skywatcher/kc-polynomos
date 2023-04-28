from polynomos.base_callable import BaseCallable
from polynomos.lists.plainlist import PlainList
from polynomos.polynomials.polys import Polynomial
from polynomos.polynomials.monomials import Monomial

__all__ = [
    'UnivariatePoly',
    'Var',
    'Vars',
    'MultiPoly'
]

class UnivariatePoly(BaseCallable):
    @staticmethod
    def eval(coeffs: PlainList, symbol: str = 'x', **kwargs):
        coeffs = coeffs._list
        i = 0
        
        monomials = []
        for i, _ in enumerate(coeffs):
            monomials.append(Monomial({symbol: i}))

        return Polynomial(monomials, coeffs)
    
class Var(BaseCallable):
    @staticmethod
    def eval(symbol: str, **kwargs):
        return Polynomial([Monomial({symbol: 1})], [1])
    
class Vars(BaseCallable):
    def __new__(cls, symbols: str, delimiter: str = ' ', **kwargs) -> None:
        return cls.eval(symbols, delimiter=delimiter, **kwargs)

    @staticmethod
    def eval(symbols: str, delimiter: str = ' ', **kwargs):
        symbols_list = symbols.split(delimiter)
        return tuple(map(Var, symbols_list))
    
class MultiPoly(BaseCallable):
    @staticmethod
    def eval(coeff_dict, **kwargs):
        monomials = []
        coeffs = []

        for monomial, coeff in coeff_dict.items():
            monomial = {key: value for key, value in monomial}
            monomials.append(Monomial(monomial))
            coeffs.append(coeff)

        return Polynomial(monomials, coeffs)