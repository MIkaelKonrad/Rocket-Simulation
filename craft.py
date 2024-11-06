from engine import Merlin

class Craft:
    def __init__(self,engine,payload,add_weight,tank_mat_density,tank_thickness, radius):
        self.add_weight_weight = add_weight
        self.engine = engine
        self.payload = payload
        self.tot_weight= engine.weight + payload + add_weight
        self.tank_mat_density = tank_mat_density
        self.radius = radius
        self.tank_thickness = tank_thickness



Falcon_9_payload = 15000000
Falcon_9_add_weight= 100000
Falcon_9_tank_mat_density = 4.5 # density of titanium in g/ccm
Falcon_9_tank_thickness = 0.1 # in cm 
Falcon_9_radius = 300 # in cm falcon 9 diameter 3.7m
Falcon_9 = Craft(Merlin,Falcon_9_payload, Falcon_9_add_weight,Falcon_9_tank_mat_density,Falcon_9_tank_thickness,Falcon_9_radius )


        
