import numpy as np
from datetime import datetime


def get_dc(date, T, r0, D0, SH=True):

    month = int(datetime.strptime(date, '%Y%m%d').strftime("%m"))

    rd = 0.83*r0 - 1.27
    Qo = 800*np.exp(-D0/400)
    Qr = Qo + 3.937*rd
    dr1 = 400*np.log(800/Qr)   # dr1

    if dr1 > 0:
        do = dr1
    else:
        do = 0

    if (r0 > 2.8):
        Do = do
    else:
        Do = D0

    # Lf
    day_duration_south = [6.4, 5, 2.4, 0.4, -1.6, -1.6, -1.6, -1.6, -1.6, 0.9, 3.8, 5.8]
    day_duration_north = [1.6, -1.6, -1.6, 0.9, 3.8, 5.8, 6.4, 5, 2.4, 0.4, -1.6, -1.6]

    if SH is True:
        Lf = day_duration_south[month]
    else:
        Lf = day_duration_north[month]


    # evapotranspiración potencial
    V = 0.36 * (T + 2.8) + Lf
    if T > -2.8:
        V = 0.36 * (T + 2.8) + Lf  # Lf = T14
    else:
        V = Lf

    if V < 0:
        V = 0

    # D = 400*np.log(800/Q)
    D = Do + 0.5*V      # N14 = Do and M14 = V

    return D
