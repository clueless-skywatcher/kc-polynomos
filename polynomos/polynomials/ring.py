class PolynomialRing:
    '''
    Represents a ring R[x1, x2, ..., xn] of polynomials in n variables
    '''
    def __init__(self, symbols) -> None:
        self.symbols = symbols

    @staticmethod
    def from_string(symbols: str):
        symbol_list = symbols.split(" ")
        return PolynomialRing(symbol_list)

    def variables(self):
        return tuple(self.symbols)
    
    def var_count(self):
        return len(self.symbols)