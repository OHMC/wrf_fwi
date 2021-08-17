import numpy as np


def get_isi(F, W):
    """ Gompute the propatation initial index
    """
    m = 147.2*(101 - F)/(59.5 + F)  # contenido de humedad del compustible fino
    fw = np.exp(0.05038*W)
    fF = 91.9*np.exp(-0.1386*m)*(1 + np.power(m, 5.31)/(4.93*np.power(10, 7)))

    R = 0.208*fF*fw

    return R