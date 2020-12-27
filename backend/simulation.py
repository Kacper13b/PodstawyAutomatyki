from backend.config import config
import numpy as np


def simulation():
    config.initialize_simulation_cycles()
    config.initialize_arrays()
    for index in range(np.int(config.get_simulation_cycles())):
        pass
    pass
