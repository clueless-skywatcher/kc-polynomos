from polynomos.base_callable import BaseCallable
from polynomos.lists.plainlist import PlainList
from polynomos.polynomials.polys import Polynomial
from polynomos.polynomials.monomials import Monomial

class UnivariatePoly(BaseCallable):
    @staticmethod
    def eval(coeffs: PlainList, symbol: str = 'x', **kwargs):
        coeffs = coeffs._list
        i = 0
        while i < len(coeffs):
            if coeffs[i] == 0:
                i += 1
            else:
                break

        coeffs = coeffs[i:]
        
        monomials = []
        for i, _ in enumerate(coeffs):
            monomials.append(Monomial({symbol: i}))

        return Polynomial(monomials, coeffs)
    
class Var(BaseCallable):
    @staticmethod
    def eval(symbol: str, **kwargs):
        return Polynomial([Monomial({symbol: 1})], [1])
    
class Vars(BaseCallable):
    @staticmethod
    def eval(symbols: str, delimiter: str = ' ', **kwargs):
        symbols_list = symbols.split(delimiter)
        return map(Var, symbols_list)
    
class MultiPoly(BaseCallable):
    @staticmethod
    def eval(coeff_dict, **kwargs):
        monomials = []
        coeffs = []

        for monomial, coeff in coeff_dict.items():
            monomials.append(Monomial(monomial))
            coeffs.append(coeff)

        return Polynomial(monomials, coeffs)