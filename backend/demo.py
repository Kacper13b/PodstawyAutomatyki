from backend.config import config
from backend.plots import plot
from backend.simulation import simulation
from backend.plots import plot



def set_demo_config():
    config.set_time(5)
    config.set_initial_temperature(24)
    config.set_temperature_goal(80)
    config.set_ambient_temperature(24)
    config.set_current_water_temperature(24)
    config.initialize_simulation_cycles()


def demo():
    simulation()
    print("xxx")

