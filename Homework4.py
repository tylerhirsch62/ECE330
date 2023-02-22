import mymath as math
from math import sqrt
from sympy import Eq, Symbol, solve

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
    Va = Symbol('Va')
    eq = Eq((N1 * i1 - Va) / R1 + (N2 * i2 - Va) / R2 - Va / R3, 0)
    Va = solve(eq)[0]
    print(Va)
    flux1 = (N1 * i1 - Va) / R1 + Va / R2 - (N2 * i2 - Va) / R2
    fluxlinkage1 = N1 * flux1
    fluxlinkage2 = inductance2 * i2 / 1000
    print("Flux linkage 1: " + str(fluxlinkage1))
    print("Flux linkage 2: " + str(fluxlinkage2))

def p3(W: float, D: float, N1: int, N2: int, g: float, i1: float, i2: float, x = float) -> None:
    W /= 100; D /= 100; g /= 100; x/= 100
    airarea1 = D * W
    airarea2 = D * W
    airReluctance1 = g / (math.mu * airarea1) / 10**6
    airReluctance2 = x / (math.mu * airarea2) / 10**6
    flux1 = (N1 * i1 - N2 * i2) / airReluctance1 / 10**6
    flux2 = N2 * i2 / (2 * airReluctance2) / 10**6 + (N2 * i2 - N1 * i1) / airReluctance1 / 10**6
    fluxlinkage1 = flux1 * N1
    fluxlinkage2 = flux2 * N2
    print("Flux linkage 1: " + str(fluxlinkage1))
    print("Flux linkage 2: " + str(fluxlinkage2))

def p4(A: float, B: int, R1: int, R2: int, V: float) -> None:
    Res1 = math.vector(R1, 2* (B + A))
    Res2 = math.vector(0, -2 * A)
    Res3 = math.vector(R2, 2 * (B + A))
    Vol = math.vector(V, 0)
    Var1 = math.divideint(1, Res1)
    Var2 = math.divideint(1, Res2)
    Var3 = math.divideint(1, Res3)
    Var4 = math.dividevec(Vol, Res1)
    V = math.dividevec(Var4, math.addvec([Var1, Var2, Var3]))
    V2 = math.divideint(4, math.vector(4, 2.54))
    ans = math.multiplyvec(V, V2)
    print("Voltage across resistor 2: " + str(ans.mag))
    print("Voltage angle across resister 2: " + str(ans.angle))

def p5(L1: float, L2: float) -> None:
    selfinductance = (L1 + L2) / 4 * 1000
    print("Self inductance: " + str(selfinductance))
    mutualinductance = (L1 - (2 * selfinductance / 1000)) / 2 * 1000
    print("Mutual inductance: " + str(mutualinductance))
    couplingcoefficient = mutualinductance / selfinductance
    print("Coupling coefficient: " + str(couplingcoefficient))


# p2(2.3, 1.5, 1.8, 150, 146, 2.3, 2.7)
# p3(3.1, 2.6, 115, 212, 0.41, 3, 7, 0.33)
p4(0.1, 2, 1, 3, sqrt(2)*200)
# p5(0.09, 0.049)
