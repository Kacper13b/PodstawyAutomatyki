import numpy as np


class Config:

    thermal_capacity = np.float32()
    current_water_temperature = np.float32()
    temperature_goal = np.float32()
    initial_temperature = np.float32()
    time = np.float32()
    ambient_temperature = np.float32()
    time_constant = np.int(555)
    frequency = np.float32()
    delivered_heat = np.float32()
    heat_loss = np.float32()
    thermal_resistance = np.float32()
    simulation_cycles = None
    control_error_list = None           # Uchyb regulacji
    control_quantity_list = None        # Wielkość sterująca
    temperature_list = None

    Kp = 1110
    Ki = 0.05
    Kd = 5

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
        self.delivered_heat = inputted_value

    def get_delivered_heat(self):
        return self.delivered_heat

    def set_current_water_temperature(self, inputted_value):
        self.current_water_temperature = inputted_value

    def get_current_water_temperature(self):
        return self.current_water_temperature

    def set_heat_loss(self, inputted_value):
        self.heat_loss = inputted_value

    def get_heat_loss(self):
        return self.heat_loss

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
        self.simulation_cycles = np.float32(self.time * 60.0 * 60.0)

    def initialize_arrays(self):
        self.control_error_list = np.array([0.0] * int(self.get_simulation_cycles()))
        self.control_quantity_list = np.array([0.0] * int(self.get_simulation_cycles()))
        self.temperature_list = np.array([0.0] * int(self.get_simulation_cycles() + 1))
        self.temperature_list[0] = self.get_initial_temperature()


config = Config()
# config.set_time(1.0)
# config.initialize_simulation_cycles()
# config.initialize_arrays()
# print(config.control_quantity.size)
print(np.float32("32") * 2.0)
