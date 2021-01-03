from backend.config import config
from backend.simulation import simulation


def set_demo_config():
    config.set_time(5)
    config.set_initial_temperature(23)
    config.set_temperature_goal(100)
    config.set_ambient_temperature(24)
    config.set_current_water_temperature(24)
    config.initialize_simulation_cycles()
    config.set_thermal_capacity(200)
    config.set_thermal_resistance(10)


def demo():
    simulation()


set_demo_config()
demo()
