from backend.config import config
import numpy as np


def simulation():
    config.initialize_simulation_cycles()
    config.initialize_arrays()
    K = 0.06
    Ki = 0.05
    T_zad = 100
    tau = 555
    Kd = 5
    Ta = 21
    Rt = K
    masa = 3
    CT = tau/Rt
    N = np.int(config.get_simulation_cycles())
    e = [0] * (N)
    U = [0] * N
    Qw = [0] * N
    Qa = [0.0] * N
    T = [0] * (N + 1)
    Kp = 1110
    T[0] = Ta
    e[0] = 0
    sum_e = 0
    Tp = 1/10
    Ti = Kp/Ki
    Td = Kd/Kp
    c = 4200
    for n in range(np.int(config.get_simulation_cycles())/Tp):
        e[n] = T_zad - T[n]
        sum_e += e[n]
        if n == 0:
            delta_e = e[n]
        else:
            delta_e = e[n] - e[n - 1]
        U[n] = Kp * (e[n] + Tp / Ti * sum_e + Td / Tp * delta_e)
        Qw[N] = 0.05 * U[n]
        Qa[N] = (T[n]-Ta)/Rt
        T[n+1] = ((Qw[n]-Qa[n])/CT)*Tp + T[n]
    # print(T[-1])
