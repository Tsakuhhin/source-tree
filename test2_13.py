from time import *

def bittvektorite_generaator(n, vektor = ""):
    if len(vektor) == n:
        return 1
    return bittvektorite_generaator(n, vektor + "0") + bittvektorite_generaator(n, vektor + "1")

a = time()
bittvektorite_generaator(24, vektor="")
b = time()
aeg = b-a
print("aeg:", aeg)
