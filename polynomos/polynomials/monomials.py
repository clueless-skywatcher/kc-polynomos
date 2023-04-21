from polynomos.polynomials.ring import PolynomialRing

class Monomial:
    def __new__(cls, power_dict: dict):
        if all([value == 0 for key, value in power_dict.items()]):
            return 1
        else:
            return super(Monomial, cls).__new__(cls)

    def __init__(self, power_map: dict) -> None:
        self.power_map = power_map
        self.symbols = sorted(power_map.keys())

        self._sorted_degrees = [self.power_map[key] for key in self.symbols]

    def __str__(self):
        end_repr = ""
        sorted_power_map = sorted(self.power_map.items(), key = lambda x: x[0])
        for symbol, power in sorted_power_map:
            if power == 1:
                end_repr += f"{symbol}"
            elif power > 0:
                end_repr += f"{symbol}^{power}"

        return end_repr
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, other):
        if not isinstance(other, Monomial):
            return False
        
        cleaned_power_self = {key: value for key, value in self.power_map.items() if value != 0}
        cleaned_power_other = {key: value for key, value in other.power_map.items() if value != 0}

        return cleaned_power_self == cleaned_power_other
    
    def __ne__(self, other):
        if not isinstance(other, Monomial):
            return False
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if not isinstance(other, Monomial):
            raise ValueError(f"Cannot compare monomial to: {type(other)}")
        return self._sorted_degrees < other._sorted_degrees
    
    def __gt__(self, other):
        if not isinstance(other, Monomial):
            raise ValueError(f"Cannot compare monomial to: {type(other)}")
        return self._sorted_degrees > other._sorted_degrees
    
    def __le__(self, other):
        if not isinstance(other, Monomial):
            raise ValueError(f"Cannot compare monomial to: {type(other)}")
        return self._sorted_degrees <= other._sorted_degrees
    
    def __ge__(self, other):
        if not isinstance(other, Monomial):
            raise ValueError(f"Cannot compare monomial to: {type(other)}")
        return self._sorted_degrees >= other._sorted_degrees
    
    def __mul__(self, other):
        if not isinstance(other, Monomial):
            raise TypeError("Can only multiply monomials with monomials")
        
        new_power_map = self.power_map.copy()
        for symbol in other.power_map:
            if symbol not in new_power_map:
                new_power_map[symbol] = other.power_map[symbol]
            else:
                new_power_map[symbol] = new_power_map[symbol] + other.power_map[symbol]

        return Monomial(new_power_map)
    
    def __rmul__(self, other):
        return self.__mul__(other)