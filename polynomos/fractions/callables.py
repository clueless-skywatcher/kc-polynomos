from polynomos.base_callable import BaseCallable
from polynomos.fractions.rational import Rational

__all__ = [
    "Fraction",
    "NumericValue",
    "Rationalize"
]

class Fraction(BaseCallable):
    @staticmethod
    def eval(num: int | float | Rational, denom: int | float | Rational, auto_reduce = True, **kwargs):
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if isinstance(num, float):
            num = Rational.rationalize(num)
        if isinstance(num, Rational):
            denom = num.denom * denom
            num = num.num
        if num == 0:
            return 0
        if denom == -1:
            return -num
        if denom == 1:
            return num
        if num % denom == 0:
            return num // denom
        return Rational(num, denom, auto_reduce = auto_reduce)

class NumericValue(BaseCallable):
    @staticmethod
    def eval(x: Rational | int | float, n: int = 3):
        if isinstance(x, (int, float)):
            return round(x, n)
        return round(float(x.num / x.denom), n)
    
class Rationalize(BaseCallable):
    @staticmethod
    def eval(x: float, **kwargs):
        return Rational.rationalize(x)