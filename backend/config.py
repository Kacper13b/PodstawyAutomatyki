import numpy as np


class Config:
    time_constant = 555
    K = 0.06
    Cw = 4200
    Kp = 1110
    Ki = 0.05
    Kd = 5
    Tp = None
    Ti = Kp / Ki
    Td = Kd / Kp

    current_water_temperature = None
    temperature_goal = None
    initial_temperature = None
    time = None
    ambient_temperature = None
    thermal_resistance = K
    thermal_capacity = time_constant / thermal_resistance

    delivered_heat_list = None
    heat_loss_list = None
    simulation_cycles = None
    control_error_list = None           # Uchyb regulacji
    control_quantity_list = None        # Wielkość sterująca
    temperature_list = None
    sum_of_errors = 0

    control_quantity_minimum = 0
    control_quantity_maximum = 10

    def get_sum_of_errors(self):
        return self.sum_of_errors

    def set_thermal_capacity(self, inputted_value):
        self.thermal_capacity = inputted_value

    def get_thermal_capacity(self):
        return self.thermal_capacity

    def set_thermal_resistance(self, inputted_value):
        self.thermal_resistance = inputted_value

    def get_thermal_resistance(self):
        return self.thermal_resistance

    def set_ambient_temperature(self, inputted_value):
        self.ambient_temperature = inputted_value

    def get_ambient_temperature(self):
        return self.ambient_temperature

    def set_time(self, inputted_value):
        self.time = inputted_value

    def get_time(self):
        return self.time

    def set_time_constant(self, inputted_value):
        self.time_constant = inputted_value

    def get_time_constant(self):
        return self.time_constant

    def set_frequency(self, inputted_value):
        self.frequency = inputted_value

    def get_frequency(self):
        return self.frequency

    def set_delivered_heat(self, inputted_value):
        self.delivered_heat_list = inputted_value

    def get_delivered_heat(self):
        return self.delivered_heat_list

    def set_current_water_temperature(self, inputted_value):
        self.current_water_temperature = inputted_value

    def get_current_water_temperature(self):
        return self.current_water_temperature

    def set_heat_loss(self, inputted_value):
        self.heat_loss_list = inputted_value

    def get_heat_loss(self):
        return self.heat_loss_list

    def set_temperature_goal(self, inputted_value):
        self.temperature_goal = inputted_value

    def get_temperature_goal(self):
        return self.temperature_goal

    def set_initial_temperature(self, inputted_value):
        self.initial_temperature = inputted_value

    def get_initial_temperature(self):
        return self.initial_temperature

    def get_simulation_cycles(self):
        return self.simulation_cycles

    def get_control_error_list(self):
        return self.control_error_list

    def get_control_quantity(self):
        return self.control_quantity_list

    def initialize_simulation_cycles(self):
        self.simulation_cycles = (self.time * 60.0 * 60.0)

    def initialize_arrays(self):
        print(self.simulation_cycles)
        self.control_error_list = [0] * int(self.get_simulation_cycles())
        self.control_quantity_list = [0.0] * int(self.get_simulation_cycles())
        self.heat_loss_list = [0.0] * int(self.get_simulation_cycles())
        self.temperature_list = [0.0] * int(self.get_simulation_cycles() + 1)
        self.delivered_heat_list = [0.0] * int(self.get_simulation_cycles())
        self.temperature_list[0] = self.get_initial_temperature()
        self.Tp = 1 / self.simulation_cycles

    def initialize(self):
        self.initialize_simulation_cycles()
        self.initialize_arrays()


config = Config()
# config.set_time(1.0)
# config.initialize_simulation_cycles()
# config.initialize_arrays()
# print(config.control_quantity.size)
