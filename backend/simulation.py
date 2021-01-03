from backend.config import config
import numpy as np
import math


def minmax(minimum, maximum, value):
    return max(minimum, min(maximum, value))


def count_heat_loss(index):
    config.get_heat_loss()[index] = (
                                            config.get_current_water_temperature() - config.get_ambient_temperature()) / config.get_thermal_resistance()


def count_error(index):
    config.control_error_list[index] = config.get_temperature_goal() - config.get_current_water_temperature()


def sum_errors(value):
    config.sum_of_errors += value


def count_control_quantity_value(index):
    return config.Kp * (config.get_control_error_list()[index] + config.Tp /
                        config.Ti * config.get_sum_of_errors() + config.Td / config.Tp * find_delta_error(index))


def append_element_to_control_quantity_list(index):
    #print(minmax(config.control_quantity_minimum, config.control_quantity_maximum, count_control_quantity_value(index)))
    # try:
    config.get_control_quantity()[index] = minmax(config.control_quantity_minimum, config.control_quantity_maximum, count_control_quantity_value(index))
    # except ValueError:
    #     print("valErr")


def find_delta_error(index):
    return config.get_control_error_list()[index] - config.get_control_error_list()[index - 1]


def update_temperature(index):
    config.set_current_water_temperature((config.get_delivered_heat()[index] - config.get_heat_loss()[index]) / config.Cw * config.mass + config.get_current_water_temperature())


def count_heat_gain(index):
    config.delivered_heat_list[index] = config.get_thermal_capacity() * config.get_control_error_list()[index] / \
                                        config.Tp + config.get_current_water_temperature() / config.get_thermal_resistance() - \
                                        config.get_ambient_temperature() / config.get_thermal_resistance()


def simulation():
    config.initialize_simulation_cycles()
    config.initialize_arrays()
    for index in range(int(config.get_simulation_cycles())):
        count_error(index)
        sum_errors(config.control_error_list[index])
        append_element_to_control_quantity_list(index)
        count_heat_loss(index)
        count_heat_gain(index)
        update_temperature(index)
        print(config.current_water_temperature)
