''' This Script simulates the efficiency of stage different configurations.

    The function Stage_Sim.comp_stages() finds an efficient stage length given a certain number of stages

    The function Stage_Sim.fuel_plot() returns a plot showing how much fuel each Stage configuration requires to
    reach low earth orbit. 
    
    The function Stage_Sim.fuel_diff_polt() returns a plot of how much fuel can be saved by increasing 
    the number of stages by 1.
    '''


import fuel
import craft 
import Chemicals 
from stages import Stage
from tanks import Tank
import engine
import stages
from stage_config import Stage_Config
import matplotlib.pyplot as plt
import numpy


class Stage_Sim:
    def __init__(self,craft,base_stage,range_of_stages):
        self.craft = craft
        self.base_stage = base_stage
        self.range_of_stages=range_of_stages
        self.n = len(range_of_stages) 


    def comp_stages(self):
        self.fuel_masses = numpy.zeros(self.n)
        self.deltaVs = numpy.zeros(self.n)


        i = 0 
        for l in self.range_of_stages:
            j=0
            vect_base = numpy.ones(l)    
            deltaV = 0
            vect = vect_base * 20 
            Good = False
            while Good== False:
                vect_base = numpy.ones(l)
                if deltaV < 10000:
                    j = j + 0.5
                    vect = vect_base * j * 20 
                    Test_Stage_Config = Stage_Config(self.craft,self.base_stage,vect)
                    deltaV= Test_Stage_Config.deltaV()
                elif deltaV > 12000:
                    j = j-0.05 
                    vect = vect_base * j * 20 
                    Test_Stage_Config = Stage_Config(self.craft,self.base_stage,vect)
                    deltaV= Test_Stage_Config.deltaV()
                else:
                    Good = True 
                    self.deltaVs[i] = deltaV 
                    self.fuel_masses[i] = sum(Test_Stage_Config.M_f-Test_Stage_Config.M_e)
                    i=i+1 

    
    def fuel_plot(self):
        self.comp_stages()
        plt.plot(self.range_of_stages, self.fuel_masses)
        plt.ylabel('fuel in 10^8 g ')
        plt.xlabel('number of stages')
        plt.show()
    
    def fuel_diff_plot(self):
        self.fuel_diff()
        plt.plot(self.steps,self.fuel_diff)
        plt.ylabel('fuel in 10^8 g ')
        plt.xlabel('stage steps')
        plt.show()

    def fuel_diff(self):
        self.fuel_diff = numpy.zeros(self.n -1 )
        self.comp_stages()
        self.steps = ["" for x in range(self.n-1)]
        i = 0
        while i < self.n-1:
            self.fuel_diff[i] = self.fuel_masses[i] - self.fuel_masses[i+1]
            self.steps[i] = str(self.range_of_stages[i]) +' to ' + str(self.range_of_stages[i+1])
            i = i+1
        

        


    