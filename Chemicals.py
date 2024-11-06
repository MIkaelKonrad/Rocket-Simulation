class Chemical:
    def __init__(self,freezing,boiling,density):
        # freezing temperature in Kelvin
        self.freezing = freezing
        # boiling point in Kelvin 
        self.boiling = boiling
        # density liquid g/ccm
        self.density = density

O2 = Chemical(54.8,90.15,1.141)
RP1 = Chemical(226.15,150,0.82)

