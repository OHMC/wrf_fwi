

def get_peligros(S):
    """
    Devuelve un codigo de peligro para cada valor de S (FWI).
    FWI = S
    """
    if S <  5:
        return "B"
    elif S < 14:
        return "M"
    elif S < 27:
        return "A"
    elif S < 46:
        return "MA"
    else:
        return "E"
