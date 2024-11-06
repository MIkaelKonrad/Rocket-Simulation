''' The class Stage_Comp is used to compare different base stages. '''

import stage_sim
import stages
import matplotlib.pyplot as plt


class Stage_Comp:
    def __init__(self,base_1,base_2,base_3,craft,range_of_stages):
        self.base_1 = base_1
        self.base_2 = base_2
        self.base_3 = base_3
        self.craft = craft
        self.range_of_stages = range_of_stages
        self.rocket_1 = stage_sim.Stage_Sim(craft,base_1,range_of_stages)
        self.rocket_2 = stage_sim.Stage_Sim(craft,base_2,range_of_stages)
        self.rocket_3 = stage_sim.Stage_Sim(craft,base_3,range_of_stages)

    def fuel_plot(self):
        self.rocket_1.comp_stages()
        self.rocket_2.comp_stages()
        self.rocket_3.comp_stages()
        plt.plot(self.range_of_stages, self.rocket_1.fuel_masses, label = self.base_1.name)
        plt.plot(self.range_of_stages, self.rocket_2.fuel_masses, label = self.base_2.name)
        plt.plot(self.range_of_stages, self.rocket_3.fuel_masses, label = self.base_3.name)
        plt.ylabel('fuel in 10^8 g ')
        plt.xlabel('number of stages')
        plt.legend()
        plt.show()


