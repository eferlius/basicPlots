import matplotlib.pyplot as plt
import os
cwd = os.getcwd()
if os.path.split(cwd)[1] == 'basicPlots':
    # if in the same folder of basicPlots
    import figure_parameters
else:
    # if in external folder
    import basicPlots.figure_parameters as figure_parameters

figure_parameters.use_default_parameters('huge')
figure_parameters.see_parameters()
plt.show()