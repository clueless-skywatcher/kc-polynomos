from polynomos.fractions.rational import Rational

class Polynomial:
    def __new__(cls, *coeffs, **kwargs):
        if len(coeffs) == 0:
            return 0
        return super(Polynomial, cls).__new__(cls)

    def __init__(self, *coeffs, **kwargs) -> None:
        coeffs = list(self._remove_leading_zeros(coeffs))

        for i in range(len(coeffs)):
            if not isinstance(coeffs[i], Rational) and int(coeffs[i]) == coeffs[i]:
                coeffs[i] = int(coeffs[i])

        self._coeffs = tuple(coeffs)
        self._kwargs = kwargs

        self._symbol = 'x'

        if self._kwargs.get('symbol'):
            self._symbol = self._kwargs.get('symbol')

    def _remove_leading_zeros(self, coeffs):
        if len(coeffs) <= 1:
            return coeffs
        if all(coeff == 0 for coeff in coeffs):
            return []
        
        i = 0
        while coeffs[i] == 0 and i < len(coeffs):
            i += 1
        return coeffs[i:]


    @staticmethod
    def _is_polynomizable(x):
        return isinstance(x, (int, float, Rational,Polynomial))

    def __add__(self, other):
        if not (Polynomial._is_polynomizable(other)):
            raise ValueError("Either of the two operands is not polynomizable")
        
        if isinstance(other, (int, float, Rational)):
            other = Polynomial(other)
        
        if self._symbol != other._symbol:
            raise ValueError("Multinomial addition is not yet supported")

        if len(self._coeffs) <= len(other._coeffs):
            bigger_coeffs = other._coeffs
            smaller_coeffs = self._coeffs
        else:
            bigger_coeffs = self._coeffs
            smaller_coeffs = other._coeffs
        
        len_diff = len(bigger_coeffs) - len(smaller_coeffs)
        smaller_coeffs = [0] * len_diff + list(smaller_coeffs)

        new_poly_coeffs = []

        for a_i, b_i in zip(bigger_coeffs, smaller_coeffs):
            new_poly_coeffs.append(a_i + b_i)
        
        return Polynomial(*new_poly_coeffs, symbol = self._symbol)
    
    def _degree(self, symbol):
        if self._symbol != symbol:
            return 0
        return len(self._coeffs) - 1
    
    def __mul__(self, other):
        if not (Polynomial._is_polynomizable(other)):
            raise ValueError("Either of the two operands is not polynomizable")
        
        if isinstance(other, (int, float, Rational)):
            other = Polynomial(other, symbol = self._symbol)

        if self._symbol != other._symbol:
            raise ValueError("Multinomial multiplication is not yet supported")

        coeffs1 = self._coeffs
        coeffs2 = other._coeffs

        new_coeffs = []

        n = len(coeffs1)
        m = len(coeffs2)

        for k in range(n + m):
            new_coeff = 0
            for i in range(max(0, k - m), min(n, k)):
                new_coeff = new_coeff + coeffs1[i] * coeffs2[k - i - 1]

            new_coeffs.append(new_coeff)
        
        return Polynomial(*new_coeffs, symbol = self._symbol)
    
    def __eq__(self, other):
        if not Polynomial._is_polynomizable(other):
            return False
        if isinstance(other, (int, float, Rational)):
            other = Polynomial(other)
        return self._coeffs == other._coeffs and self._symbol == other._symbol
    
    def quot_rem(self, other, symbol):
        if not (Polynomial._is_polynomizable(other)):
            raise ValueError("Either of the two operands is not polynomizable")
        
        if isinstance(other, (int, float, Rational)):
            other = Polynomial(other, symbol = symbol)

        if symbol != other._symbol:
            raise ValueError("Multinomial division is not yet supported")
        
        coeffs1 = self._coeffs
        coeffs2 = other._coeffs
        # import pdb
        # pdb.set_trace()
        quotient_coeffs = []

        n = len(coeffs1)
        m = len(coeffs2)

        normalizer = coeffs2[0]

        quotient_coeffs = list(coeffs1).copy()

        for i in range(n - m + 1):
            quotient_coeffs[i] /= normalizer
            coef = quotient_coeffs[i]

            if coef != 0:
                for j in range(1, m):
                    quotient_coeffs[i + j] += -1 * coeffs2[j] * coef

        separator = -(m - 1)

        quot = quotient_coeffs[:separator]
        rem = quotient_coeffs[separator:]

        return Polynomial(*quot, symbol = symbol), Polynomial(*rem, symbol = symbol)
        
    def _lc(self, symbol):
        if symbol != self._symbol:
            return 0
        return self._coeffs[0]
    
    def __neg__(self):
        coeffs = [-coeff for coeff in self._coeffs]
        return Polynomial(*coeffs, symbol = self._symbol)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __rsub__(self, other):
        return -self + other
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return str(self)
    
    def _monomial_represent(self, power):
        if power == 0:
            return ""
        elif power == 1:
            return self._symbol
        return f"{self._symbol}^{power}"
    
    def __str__(self) -> str:
        monomial_str = ""
        len_coeffs = len(self._coeffs)
        if len_coeffs == 1:
            return str(self._coeffs[0])

        for i in range(len_coeffs):
            if self._coeffs[i] == 0:
                continue
            elif isinstance(self._coeffs[i], Rational):
                if self._coeffs[i] >= 0:
                    monomial_str += f" + ({self._coeffs[i].num}/{self._coeffs[i].denom}){self._monomial_represent(len_coeffs - i - 1)}"
                else:
                    monomial_str += f" - ({abs(self._coeffs[i].num)}/{abs(self._coeffs[i].denom)}){self._monomial_represent(len_coeffs - i - 1)}"
            elif self._coeffs[i] == 1 and i != len(self._coeffs) - 1:
                monomial_str += f" + {self._monomial_represent(len_coeffs - i - 1)}"
            elif self._coeffs[i] == -1 and i != len(self._coeffs) - 1:
                monomial_str += f" - {self._monomial_represent(len_coeffs - i - 1)}"
            elif self._coeffs[i] > 0:
                monomial_str += f" + {self._coeffs[i]}{self._monomial_represent(len_coeffs - i - 1)}"
            else:
                monomial_str += f" - {abs(self._coeffs[i])}{self._monomial_represent(len_coeffs - i - 1)}"

        monomial_str = monomial_str.strip()
        if monomial_str.startswith("- "):
            return monomial_str.replace("- ", "-", 1)
        return monomial_str.lstrip("+ ")