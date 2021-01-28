from backend.config import config
import numpy as np
import math
import pandas as pd
from backend.data import creatDataFrame

def minmax(minimum, maximum, value):
    return max(minimum, min(maximum, value))


def count_heat_loss(index):
    config.get_heat_loss()[index] = (config.get_current_water_temperature() - config.get_ambient_temperature()) \
                                    / config.get_thermal_resistance()


def count_error(index):
    config.control_error_list[index] = config.get_temperature_goal() - config.get_current_water_temperature()


def sum_errors(index):
    # print(index)
    # print(config.get_control_error_list()[index])
    config.sum_of_errors += config.get_control_error_list()[index]


def count_control_quantity_value(index):
    return config.Kp * (config.get_control_error_list()[index] + (config.Tp /
                        config.Ti) * config.get_sum_of_errors() + (config.Td / config.Tp) * find_delta_error(index))


def append_element_to_control_quantity_list(index):
    config.get_control_quantity()[index] = minmax(config.control_quantity_minimum, config.control_quantity_maximum, count_control_quantity_value(index))
    #config.get_control_quantity()[index] = config.Kp * (config.get_control_error_list()[index] + config.Tp / config.Ti * config.get_sum_of_errors() + config.Td / config.Tp * find_delta_error(index))


def find_delta_error(index):
    if (index == 0):
        return 0.1
    return config.get_control_error_list()[index] - config.get_control_error_list()[index - 1]


def update_temperature(index):
    # config.set_current_water_temperature((config.get_delivered_heat()[index] - config.get_heat_loss()[index]) / config.Cw * config.mass + config.get_current_water_temperature())
    config.temperature_list[index+1] = ((config.get_delivered_heat()[index] - config.get_heat_loss()[index]) / config.get_thermal_capacity()) * config.Tp +config.temperature_list[index]
    config.set_current_water_temperature(config.temperature_list[index+1])


def count_heat_gain(index):
    config.delivered_heat_list[index] = 20 * config.get_control_quantity()[index]


def simulation():
    config.initialize_simulation_cycles()
    config.initialize_arrays()
    for index in range(int(config.get_simulation_cycles())):
        count_error(index)
        sum_errors(index)
        append_element_to_control_quantity_list(index)
        count_heat_gain(index)
        count_heat_loss(index)
        update_temperature(index)
    dataFrame = creatDataFrame()


def set_simulation_config(time, initial_temp, temp_goal, ambient_temp):
    config.set_time(time)
    config.set_initial_temperature(initial_temp)
    config.set_temperature_goal(temp_goal)
    config.set_ambient_temperature(ambient_temp)
    config.set_current_water_temperature(ambient_temp)
    config.initialize_simulation_cycles()