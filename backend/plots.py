import matplotlib.pyplot as plt

def plots():
    print("In")
    plt.plot(int(config.get_simulation_cycles()), config.temperature_list)
    plt.xlabel("Liczba symulacji")
    plt.ylabel("Temperatura wody")
    plt.grid(True)
    plt.title("Temperatura wody podczas symulacji")
    plt.legend()
    plt.show()
    print("In plots")