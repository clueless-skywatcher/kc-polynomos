from polynomos.base_callable import BaseCallable

from polynomos.polynomials.poly import Polynomial

__all__ = [
    "PolynomialNew",
    "PolynomialAdd",
    "PolyCoefficientList",
    "PolyLeadingCoefficient",
    "PolynomialDegree",
    "PolynomialQuotient",
    "PolynomialRemainder",
    "PolynomialQuotientRemainder"
]

class PolynomialNew(BaseCallable):
    @staticmethod
    def eval(*coeffs, **kwargs):
        return Polynomial(*coeffs, **kwargs)
    
class PolynomialAdd(BaseCallable):
    @staticmethod
    def eval(p1, p2):
        return p1 + p2
    
class PolyCoefficientList(BaseCallable):
    @staticmethod
    def eval(p: Polynomial, symbol: str = 'x'):
        if p._symbol != symbol:
            return []
        return list(p._coeffs)
    
class PolyLeadingCoefficient(BaseCallable):
    @staticmethod
    def eval(p: Polynomial, symbol: str = 'x'):
        return p._lc(symbol)

class PolynomialDegree(BaseCallable):
    @staticmethod
    def eval(p: Polynomial | int | float, symbol: str = 'x'):
        if isinstance(p, (int, float)):
            return 0
        return p._degree(symbol)
    
class PolynomialQuotient(BaseCallable):
    @staticmethod
    def eval(p: Polynomial, q: Polynomial, symbol: str = 'x'):
        return p.quot_rem(q, symbol=symbol)[0]
    
class PolynomialRemainder(BaseCallable):
    @staticmethod
    def eval(p: Polynomial, q: Polynomial, symbol: str = 'x'):
        return p.quot_rem(q, symbol=symbol)[1]
    
class PolynomialQuotientRemainder(BaseCallable):
    @staticmethod
    def eval(p: Polynomial, q: Polynomial, symbol: str = 'x'):
        result = p.quot_rem(q, symbol=symbol)
        return result
