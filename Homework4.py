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
    Res1 = math.vector(R1, 2 * (B + A))
    print("Res1: " + math.printvec(Res1))
    Res2 = math.vector(0, -2 * A)
    print("Res2: " + math.printvec(Res2))
    Res3 = math.vector(R2, 2 * (B + A))
    print("Res3: " + math.printvec(Res3))
    Var1 = math.divideint(1, Res1)
    print("Var1: " + math.printvec(Var1))
    Var2 = math.divideint(1, Res2)
    print("Var2: " + math.printvec(Var2))
    Var3 = math.divideint(1, Res3)
    print("Var3: " + math.printvec(Var3))
    Vol = math.vector(V, 0)
    print(" Vol: " + math.printvec(Vol))
    Var4 = math.dividevec(Vol, Res1)
    print("Var4: " + math.printvec(Var4))
    V = math.dividevec(Var4, math.addvec([Var1, Var2, Var3]))
    print("   V: " + math.printvec(V))
    V2 = math.dividevec(V, Res3)
    print("  V2: " + math.printvec(V2))
    ans = math.multiplyint(R2, V2)
    print(" ans: " + math.printvec(ans))
    print("Voltage across resistor 2: " + str(ans.mag))
    print("Voltage angle across resister 2: " + str(360 - ans.angle))

def p5(L1: float, L2: float) -> None:
    selfinductance = (L1 + L2) / 4 * 1000
    print("Self inductance: " + str(selfinductance))
    mutualinductance = (L1 - (2 * selfinductance / 1000)) / 2 * 1000
    print("Mutual inductance: " + str(mutualinductance))
    couplingcoefficient = mutualinductance / selfinductance
    print("Coupling coefficient: " + str(couplingcoefficient))


# p2(2.3, 1.5, 1.8, 150, 146, 2.3, 2.7)
# p3(3.1, 2.6, 115, 212, 0.41, 3, 7, 0.33)
p4(0.55, 1.5, 1, 6, 160)
# p5(0.09, 0.049)
