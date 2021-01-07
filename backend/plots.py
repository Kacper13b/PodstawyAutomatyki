import matplotlib.pyplot as plt

from backend.config import config


def plot():
    print("In")
    plt.plot(range(0,int(config.get_simulation_cycles()+1)), config.temperature_list)
    plt.xlabel("Liczba symulacji")
    plt.ylabel("Temperatura wody")
    plt.grid(True)
    plt.title("Temperatura wody podczas symulacji")
    plt.legend()
    plt.show()
    print("In plots")