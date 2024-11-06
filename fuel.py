import Chemicals
class BiProp:
    def __init__(self,oxidizer,fuel,oxidizer_fuel_ratio):
        self.oxidizer = oxidizer
        self.fuel = fuel
        self.ratio = oxidizer_fuel_ratio
        self.BiProp = True


class MonoProp:
    def __init__(self,chemical):
        self.chemical = chemical
        self.BiProp = False





LOX_RP1 = BiProp(Chemicals.O2,Chemicals.RP1,2.56 )
        