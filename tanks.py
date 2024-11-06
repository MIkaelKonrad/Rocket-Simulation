''' This Script is for simulating cylindrical propellant tanks. It defines a class Tank for holding 
    the information on tanks. Tank also computes the volume a tank depending on its size.
    
    Note:   In case of the Biprop Tank actualle simulates two tanks one for the fuel and the other
            for the oxidizer.
'''

import math
import fuel


# The function below is used to calculate the volume of a cylinder, this is useful as the tanks are assumed to be cylinders.
def vol_cylinder(height,radius):
    vol=math.pi*((radius)**2) * height
    return vol


class Tank:
    def __init__(self, radius, height, density_mat, thickness, fuel):
        self.radius = radius
        self.height = height
        self.density_mat =density_mat
        self.thickness = thickness
        self.fuel = fuel
        self.tot_volume = vol_cylinder(height,radius)
        # below we compute the weights and volumes of a tank
        # note that in the case of a BiProp we need two tanks 
        # in that case we assume two cylindrical tanks stacked on top of each other
        if fuel.BiProp == False:
            self.fuel_volume = vol_cylinder(height-2*thickness,radius - thickness)
            self.weight_empty = (self.tot_volume-self.fuel_volume)*density_mat
            self.weight_full = self.weight_empty + self.fuel_volume*self.fuel.chemical.density
        else:
            tank_ratio = self.fuel.ratio/(self.fuel.ratio +1 )
            avg_density = tank_ratio*self.fuel.oxidizer.density + (1-tank_ratio)*self.fuel.fuel.density
            int_height = height-4*thickness
            vol_tank = vol_cylinder(int_height,self.radius-self.thickness)
            self.weight_empty = density_mat*(self.tot_volume-vol_tank)   
            self.weight_full = self.weight_empty + vol_tank*avg_density