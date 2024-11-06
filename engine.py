''' This Script defines a class the holds the information on the engine. '''
import fuel

class Engine:
    def __init__(self,weight,exhaust_velocity,fuel):
        self.weight = weight
        self.exhaust_velocity = exhaust_velocity
        self.fuel = fuel

Merlin_weight = 470000 #weight of merlin engine in g
#exhaust velocity from wikipedia article on the De Laval nozzle
Merlin = Engine(Merlin_weight,304.8*9.81,fuel.LOX_RP1)

