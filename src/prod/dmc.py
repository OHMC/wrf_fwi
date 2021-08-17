import numpy as np
from datetime import datetime


def get_dmc(date: str, T, H, P0, r0, SH=True):
    """ Qué es SH?
    """

    month = int(datetime.strptime(date, '%Y%m%d').strftime("%m"))

    if P0 <= 33:
        b = 100/(0.5 + 0.3*P0)
    elif P0 <= 65:
        b = 4-1.3*np.log(P0)
    else:
        b = 6.2*np.log(P0) - 17.2

    if r0 <= 1.5:
        P = P0
    else:
        # Preguntar porque es asi?
        P = 43.43*(5.6348 - np.log((20 + 280/np.exp(0.023*P0) + 1000*(0.92*r0 - 1.27)/(48.77 + b*(0.92*r0 - 1.27))) - 20))

    if P < 0:
        P = 0

    if T < -1.1:
        T = -1.1

    day_factor_south = [11.5, 10.5, 9.2, 7.9, 6.8, 6.2, 6.5, 7.4, 8.7, 10, 11.2, 11.8]
    day_factor_north = [6.5, 7.5, 9, 12.8, 13.9, 13.9, 12.4, 10.9, 9.4, 8, 7, 6]

    if SH is True:
        day_factor = day_factor_south[month]
    else:
        day_factor = day_factor_north[month]

    # Porque no es (T+1.1)?
    K = P + 1.894*T*(100 - H)*day_factor*0.0001

    if K < 0:
        return 0
    else:
        return K