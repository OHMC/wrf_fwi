import numpy as np


def get_bui(P, D):
    """ P = DMC - D = DC
        Indice de combustible disponible
    """

    """
    CONSULTAR: ·Cuando el DMC es cero, se considera que el BUI es cero sin importar el valor de DC"
    """
    if (P==0) and (D==0):
        U = 0
    else:
        U = 0.8*D*P/(P+0.4*D)          # CONSULTAR porque no es cuando P <= 0.4D

    if U < P:
        temp = P - (0.92 + np.power((0.0114*P), 1.7))*((P - U)/P)
    else:
        temp = U
    
    if temp < 0:
        temp = 0

    return temp
