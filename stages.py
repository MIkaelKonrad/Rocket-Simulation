''' This Script contains two classes, which are used to resemble stages in the simulation:
        1.  BaseStage:  This class holds the information of what the requirements for a stage are,
                        independent of the size of the propellent tanks.
        2.  Stage:      This class holds the information on a finished stage including the propellent tanks
             '''
             
from tanks import Tank
from tanks import vol_cylinder
import math
class BaseStage:
    def __init__(self, mass, density_mat, thickness, radius,length,name):
        self.mass = mass
        self.density_mat = density_mat
        self.thickness = thickness
        self.mass_per_length = density_mat*(vol_cylinder(1,radius + thickness) - vol_cylinder(1,radius))
        self.name = name
        self.length = length


class Stage:
    def __init__(self,base,tank):
        #mass of equippent needed in any Stage regardless of size
        self.base_mass = base.mass
        #mass of 1m of additional length empty
        self.mass_per_length = base.mass_per_length
        self.base_length= base.length
        self.fuel = tank.fuel 
        self.length = tank.height + base.length
        self.tank = tank
        mass_mod_tank = self.base_mass + self.mass_per_length*tank.height
        self.total_mass_empty =  mass_mod_tank + self.tank.weight_empty
        self.total_mass_full = mass_mod_tank + self.tank.weight_full

length = 100 # not important at the moment

mass_Falcon = 1000000 # base weight of a stage in g
mass_2 = 100000
mass_3 = 10000

Falcon_9_density_mat = 2.7 # aluminum in g/ccm
Falcon_9_thickness = 0.5 
Falcon_9_radius=300

Falcon_9_Base = BaseStage(mass_Falcon, Falcon_9_density_mat, Falcon_9_thickness, Falcon_9_radius,length, 'Falcon heavy')
Base_2 = BaseStage(mass_2, Falcon_9_density_mat, Falcon_9_thickness, Falcon_9_radius,length, 'Falcon light')
Base_3 = BaseStage(mass_3, Falcon_9_density_mat, Falcon_9_thickness, Falcon_9_radius,length, 'Falcon  very light')