from polynomos.integers.callables import NumQ
from polynomos.polynomials.monomials import Monomial

class Polynomial:
    def __init__(self, monomials: list[Monomial], coeffs: list) -> None:
        if not len(monomials) == len(coeffs):
            raise ValueError("Monomial list should be same as number of coefficients")
        self.coeffs = coeffs

        self.symbols = set()
        for monomial in monomials:
            self.symbols |= set(monomial.symbols)

        self.monomials = []

        for monomial in monomials:
            new_monomial = {}
            for symbol in self.symbols:
                new_monomial[symbol] = monomial.power_map.get(symbol, 0)
            self.monomials.append(Monomial(new_monomial))

        tuples_ = sorted(
            [
                (monomial, coeff) 
                for coeff, monomial in zip(self.coeffs, self.monomials)
                if coeff != 0
            ],
            key = lambda x: x[0]
        )

        self.monomials = [x[0] for x in tuples_]
        self.coeffs = [x[1] for x in tuples_]

    @staticmethod
    def is_zero(expr):
        if expr == 0:
            return 0
        if isinstance(expr, Polynomial):
            return all([value == 0 for value in expr.coeffs]) or expr.coeffs == []
        return False

    def _is_constant_monomial(self, monomial: Monomial):
        return all([monomial.power_map[x] == 0 for x in monomial.power_map])

    def __repr__(self) -> str:
        end_str = ""

        for coeff, monomial in zip(self.coeffs, self.monomials):
            if coeff == 0:
                continue
            elif coeff == 1:
                end_str += f" + {str(monomial)}"
            elif coeff == -1:
                end_str += f" - {str(monomial)}"
            elif coeff < 0:
                end_str += f" - {str(-1 * coeff)}{str(monomial)}"
            else:
                end_str += f" + {str(coeff)}{str(monomial)}"

        return end_str.strip(" +")
    
    def __add__(self, other):
        self_monomials = self.monomials.copy()
        self_coeffs = self.coeffs.copy()
            
        if NumQ(other):
            if other == 0:
                return self
            new_monomial = {symbol: 0 for symbol in self.symbols}
            other = Polynomial([Monomial(new_monomial)], [other])

        if isinstance(other, Polynomial):
            other_monomials = other.monomials
            other_coeffs = other.coeffs
            
            new_monomials = []
            new_coeffs = []

            len1 = len(self_monomials)
            len2 = len(other_monomials)

            i = 0
            j = 0

            while i < len1 or j < len2:
                if (i < len1 and j < len2) and self_monomials[i] == other_monomials[j]:
                    new_monomials.append(self_monomials[i])
                    new_coeffs.append(self_coeffs[i] + other_coeffs[j])
                    i += 1
                    j += 1
                elif (i == len1) or (j < len2 and self_monomials[i] > other_monomials[j]):
                    new_monomials.append(other_monomials[j])
                    new_coeffs.append(other_coeffs[j])
                    j += 1
                else:
                    new_monomials.append(self_monomials[i])
                    new_coeffs.append(self_coeffs[i])
                    i += 1

            return Polynomial(new_monomials, new_coeffs)
        else:
            raise TypeError(f"Cannot add Polynomial to {type(other)}")
        
    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        # import pdb
        # pdb.set_trace()
        if Polynomial.is_zero(other):
            return 0
        
        if NumQ(other):
            if other == 0:
                return self
            new_monomial = {symbol: 0 for symbol in self.symbols}
            other = Polynomial([Monomial(new_monomial)], [other])

        poly1 = self
        poly2 = other

        if len(poly2.monomials) > len(poly1.monomials):
            poly1, poly2 = poly2, poly1

        l1, l2 = len(poly1.monomials), len(poly2.monomials)

        if l2 == 1:
            return Polynomial(
                [poly2.monomials[0] * monomial for monomial in poly1.monomials],
                [poly2.coeffs[0] * coeff for coeff in poly1.coeffs]
            )
        else:
            h1 = poly2.monomials[:l2 // 2]
            h2 = poly2.monomials[l2 // 2:]

            c1 = poly2.coeffs[:l2 // 2]
            c2 = poly2.coeffs[l2 // 2:]

            return poly1 * Polynomial(h1, c1) + poly1 * Polynomial(h2, c2)
        
    def __rmul__(self, other):
        return self.__mul__(other)

        
