import numpy as np


def get_fwi(R, U):
    """
    ISI = R, BUI = U
    """
    fD = 1000/(25 + 108.64*np.exp(-0.023*U))

    if (U > 80):
        B = 0.1*R*fD
    else: 
        B = 0.1*R*(0.626*np.power(U, 0.809) + 2)

    if(B <= 1):
        S = B
    else:
        S = np.exp(2.72*np.power(0.434*np.log(B), 0.647))

    # NOTA: cualquier valor de FWI menor a 0.5 va a ser reportado como cero
    if S < 0.5:
        S = 0

    return S
