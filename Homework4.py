import mymath as math

def p1(N: int, g: float, d: float, length: float, mu: int, i: float) -> None:
    g /= 100; d /= 100; length /= 100; mu = math.mu * mu * 10**6
    corearea = 3/100 * d
    Rc = length / (mu * corearea)
    print("Relectance of core: " + str(Rc))
    airarea = (3/100 + g) * (d + g)
    Ra = g / (math.mu * airarea) / 10**6
    print("Reluctance of air gap: " + str(Ra))
    flux_linkage = N * N * i / (2 * Ra + Rc) / 10**6
    print("Flux linkage: " + str(flux_linkage))
    coilinductance = flux_linkage / i * 1000
    print("Coil Inductance: " + str(coilinductance))

def p2(R1: float, R2: float, R3: float, N1: int, N2: int, i1: float, i2: float) -> None:
    R1 *= 10**6; R2 *= 10**6; R3 *= 10**6
    inductance1 = N1 * N1 / (R1 + (1/R2 + 1/R3)**-1) * 1000
    inductance2 = N2 * N2 / (R2 + (1/R3 + 1/R1)**-1) * 1000
    print("Inductance 1: " + str(inductance1))
    print("Inductance 2: " + str(inductance2))
    fluxlinkage1 = inductance1 * i1 / 1000
    fluxlinkage2 = inductance2 * i2 / 1000
    print("Flux linkage 1: " + str(fluxlinkage1))
    print("Flux linkage 2: " + str(fluxlinkage2))

def p3(W: float, D: float, N1: int, N2: int, g: float, i1: float, i2: float, x = float) -> None:
    W /= 100; D /= 100; g /= 100
    airarea1 = (g + D) * (g + W)
    airarea2 = (x + D) * (x + W)
    airReluctance1 = g / (math.mu * airarea1) / 10**6
    airReluctance2 = x / (math.mu * airarea2) / 10**6
    print("Reluctance of the air1: " + str(airReluctance1))
    print("Reluctance of the air2: " + str(airReluctance2))
    fluxlinkage1 = N1 * N1 * i1 / (airReluctance1 + 2 * airReluctance2) / 10**6
    fluxlinkage2 = N2 * N2 * i2 / (1/airReluctance1 + 0.5/airReluctance2)**-1 / 10**6
    print("Flux linkage 1: " + str(fluxlinkage1))
    print("Flux linkage 2: " + str(fluxlinkage2))

def p4(A: float, B: int, R1: int, R2: int, V: float) -> None:
    print("Voltage across resistor 2: ")
    print("Voltage angle across resister 2: ")

def p5(L1: float, L2: float) -> None:
    print("Self inductance: ")
    print("Mutual inductance: ")
    print("Coupling coefficient: ")


# p2(1, 2.5, 2.7, 140, 130, 3.9, 3.7)
p3(4.5, 1.6, 222, 186, 0.21, 6, 3, 0.12)