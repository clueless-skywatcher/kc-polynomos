from polynomos.integers.callables import GCD

class Rational:
    def __init__(self, num, denom, auto_reduce = True) -> None:
        if auto_reduce:
            gcd = GCD(abs(num), abs(denom))
            num = num // gcd
            denom = denom // gcd
        if denom < 0:
            num = -int(abs(num))
            denom = int(abs(denom))

        self.num = num
        self.denom = denom
        

    def __str__(self):
        return f"Rational({self.num}, {self.denom})"
    
    def __repr__(self):
        return f"Rational({self.num}, {self.denom})"

    @staticmethod
    def rationalize(x: float, auto_reduce = True):
        decimal_place = str(x)[::-1].find('.')
        r_num = int(x * (10 ** decimal_place))
        r_denom = 10 ** decimal_place

        return Rational(r_num, r_denom, auto_reduce=auto_reduce)

    def __add__(self, other):
        if isinstance(other, int):
            return Rational(self.num + self.denom * other, self.denom)
        elif isinstance(other, Rational):
            return Rational(self.num * other.denom + other.num * self.denom, self.denom * other.denom)
        elif isinstance(other, float):
            rationalized_other = Rational.rationalize(other)
            return self + rationalized_other
        
        return other + self
    
    def __neg__(self):
        if self.denom == 1:
            return self.num
        elif self.denom == -1:
            return -self.num
        return Rational(self.num, self.denom)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.num == other and self.denom == 1
        if isinstance(other, float):
            other = Rational.rationalize(other)

        return self.num == other.num and self.denom == other.denom
    
    def __mul__(self, other):
        if isinstance(other, int):
            if other == self.denom:
                return self.num
            return Rational(self.num * other, self.denom)
        elif isinstance(other, Rational):
            return Rational(self.num * other.num, self.denom * other.denom)
        elif isinstance(other, float):
            rationalized_other = Rational.rationalize(other)
            return self * rationalized_other
        
        return other * self
    
    def inverse(self):
        if self.num == 1:
            return self.denom
        return Rational(self.denom, self.num)
    
    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if isinstance(other, int):
            return self.__mul__(Rational(1, other))
        elif isinstance(other, float):
            other = Rational.rationalize(other)
        return self.__mul__(other.inverse())
    
    def __rmul__(self, other):
        return self.__mul__(other)