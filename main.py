import sys
import os
from string import join
from firn_density_spin import FirnDensitySpin
from firn_density_nospin import FirnDensityNoSpin

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        configName = os.path.join(os.path.dirname(__file__), sys.argv[1])
    else:
        configName = os.path.join(os.path.dirname(__file__), 'generic.json')

    if '-s' in sys.argv:
        firn = FirnDensitySpin(configName)
        firn.time_evolve()
    else:
        firn = FirnDensityNoSpin(configName)
        firn.time_evolve()