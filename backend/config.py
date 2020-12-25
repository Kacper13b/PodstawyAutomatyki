import numpy as np


class Config:

    thermal_capacity = np.float32()
    current_water_temperature = np.float32()
    time = np.float32()
    ambient_temperature = np.float32()
    time_constant = np.float32()
    frequency = np.float32()
    delivered_heat = np.float32()
    heat_loss = np.float32()
    thermal_resistance = np.float32()
    Kp = 1110
    Ki = 0.05
    Kd = 5

    def set_thermal_capacity(self, inputted_value):
        self.thermal_capacity = inputted_value

    def set_thermal_resistance(self, inputted_value):
        self.thermal_resistance = inputted_value

    def set_ambient_temperature(self, inputted_value):
        self.ambient_temperature = inputted_value

    def set_time(self, inputted_value):
        self.time = inputted_value

    def set_time_constant(self, inputted_value):
        self.time_constant = inputted_value

    def set_frequency(self, inputted_value):
        self.frequency = inputted_value

    def set_delivered_heat(self, inputted_value):
        self.delivered_heat = inputted_value

    def set_current_water_temperature(self, inputted_value):
        self.current_water_temperature = inputted_value

    def set_heat_loss(self, inputted_value):
        self.heat_loss = inputted_value

    def get_thermal_capacity(self):
        return self.thermal_capacity

    def get_thermal_resistance(self):
        return self.thermal_resistance

    def get_ambient_temperature(self):
        return self.ambient_temperature

    def get_time(self):
        return self.time

    def get_time_constant(self):
        return self.time_constant

    def get_frequency(self):
        return self.frequency

    def get_delivered_heat(self):
        return self.delivered_heat

    def get_current_water_temperature(self):
        return self.current_water_temperature

    def get_heat_loss(self):
        return self.heat_loss


config = Config()
