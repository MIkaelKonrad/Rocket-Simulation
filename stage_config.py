from stages import Stage
from tanks import Tank
import numpy as np 
import math

class Stage_Config:
    def __init__(self,craft,base_stage,stage_lengths):
        self.n = len(stage_lengths)
        self.craft= craft
        self.base_stage = base_stage
        self.lengths = stage_lengths
        v_E = self.craft.engine.exhaust_velocity
        i=0
        r = self.craft.radius
        t_t = self.craft.tank_thickness
        fuel = self.craft.engine.fuel 
        t_m_d = self.craft.tank_mat_density
        M_e = np.zeros(self.n)
        M_f = np.zeros(self.n)
        while i < self.n:
            h = self.lengths[i]
            tank =  Tank(r, h,t_m_d ,t_t, fuel)
            stage = Stage(self.base_stage,tank)
            M_e[i] = stage.total_mass_empty
            M_f[i] = stage.total_mass_full
            i = i+1
        self.mass_rocket = sum(M_f) + self.craft.tot_weight
        self.M_e = M_e
        self.M_f = M_f


    def deltaV(self):
        i=0 
        deltaV=0
        mass_rocket=self.mass_rocket
        while i < self.n:
            variable1 = math.log(mass_rocket)
            mass_rocket = mass_rocket-self.M_f[i]
            variable2 = math.log(mass_rocket+self.M_e[i])
            loc_deltaV = self.craft.engine.exhaust_velocity * (variable1 - variable2)
            deltaV= deltaV+ loc_deltaV
            i=i+1

        return deltaV