''' This is the main script used to run the simulation. '''

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
import stage_sim
import stage_comp


craft = craft.Falcon_9
base_stage = stages.Falcon_9_Base
range_of_stages = numpy.arange(1,11,1)
Sim = stage_sim.Stage_Sim(craft,base_stage,range_of_stages)

Sim.fuel_diff_plot()

Falcon_9_Base = stages.Falcon_9_Base
Base_2 = stages.Base_2
Base_3 = stages.Base_3
#comparison = stage_comp.Stage_Comp(Falcon_9_Base,Base_2, Base_3,craft,range_of_stages)
#comparison.fuel_plot()

#stage height in cm
stage_lengths = [400,400,400,400,400]
stage_lengths_Falcon_9 = [4120,1380]


Test_Stage_Config = Stage_Config(craft,base_stage,stage_lengths)
Falcon_9_Stage_Config = Stage_Config(craft,base_stage,stage_lengths_Falcon_9)
print(Falcon_9_Stage_Config.deltaV())