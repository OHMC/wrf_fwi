import numpy as np


def get_ffmc(H, T, W, F0, r0):
    """
    TODO: - ver como se inicializa
          - corroborar-

    """

    # ------------ Fase de lluvia ----------------------------
    if (r0 > 0.5):
        rf = r0 - 0.5
    else:
        rf = 0

    if (rf > 0) and (147.2*(101-F0)/(59.5+F0) > 150):
        m0 = (147.2*(101 - F0)/(59.5 + F0)) + 42.5*(rf)*np.exp(-100/(251 - (147.2*(101 - F0)/(59.5 + F0))))*(1-np.exp(-6.93/(rf))) + 0.0015*((147.2*(101-F0)/(59.5+F0)) - 150)*((147.2*(101 - F0)/(59.5 + F0)) - 150)*np.power(rf, 0.5)
    elif (rf == 0):
        m0 = (147.2*(101 - F0)/(59.5 + F0))
    else:
        m0 = (147.2*(101 - F0)/(59.5 + F0)) + 42.5*(rf)*np.exp(-100/(251 - (147.2*(101 - F0)/(59.5 + F0))))*(1-np.exp(-6.93/(rf)))

    # Humedad de equilibrio
    Ed = (0.942*np.power(H, 0.679) + (11*np.exp((H-100)/10)) + 0.18*(21.1-T)*(1 - np.exp(-H*0.115)))
    Ew = (0.618*np.power(H, 0.753) + (10*np.exp((H-100)/10)) + 0.18*(21.1-T)*(1 - np.exp(-H*0.115)))

    k0 = 0.424*(1 - np.power((100 - H)/100, 1.7)) + 0.0694*np.power(W, 0.5)*(1 - np.power((100 - H)/100, 8))
    k = k0*0.581*np.exp(0.0365*T)

    print(f"Ew = {Ew} / Ed = {Ed} / k0 = {k0} / k= {k}")
    # m0 contenido de humedad del día anterior
    if m0 > Ed:  # régimen de secado
        m = Ed + (m0 - Ed) * np.power(10, -k)
    elif m0 < Ew:
        m = Ew - (Ew-m0)*np.power(10, -k)
    elif ((m0 > Ew) and (m0 < Ed)):
        m = m0

    """ Consultar al fer, dle excel
    if ((m0 < Ed) and (m0 > Ew)):
        m = Ew-(Ew-m0)/POTENCIA(10;k)
    elif m0>Ed:
        m = Ed+(m0-Ed)/POTENCIA(10;k)
    else:
        m = m0
    """

    F = (59.5*(250 - m)/(147.2 + m))
    if(F > 101):
        return 101
    elif(F < 0):
        return 0
    else:
        return F