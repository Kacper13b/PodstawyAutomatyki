import pandas as pd
from backend.config import config

def creatDataFrame():
    # "Temprature": config.temperature_list,
    data = {
            "Error": config.control_error_list,
            "Heat Loss": config.heat_loss_list,
            "Heat Gain": config.delivered_heat_list,
            "Control Quantity": config.control_quantity_list,
            }
    df = pd.DataFrame(data)
    return df
