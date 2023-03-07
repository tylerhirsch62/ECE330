import math

mu = 4 * math.pi * 10**-7

def p1(W, N, g, i, x, di, dx):
    W /= 100; g /= 100; x /= 100
    area = W*W
    Rg = g / (mu * area)
    Rx = x / (mu * area)
    Req = (1/Rg + 1/(2*Rx))**-1
    flux = N * i / Req
    fluxLinkage = N * flux
    print("Flux linkage: " + str(fluxLinkage))
    didt = (N**2 * di) / Req
    vt = didt - (N**2 * i * mu * area * x**-2) * dx / 2
    # vt = (N**2 * i * di) / (1/Rg + 1/(2*dRx))**-1
    print("V(t): " + str(vt))

def p2(N, g0, a0, g1, a1):
    a0 /= 100 * 100; a1 /= 100 * 100
    Rg0 = g0 / (mu * a0)
    Rg1 = g1 / (mu * a1)
    Req = Rg0 + Rg1
    Inductance = N**2 / Req
    print("Inductance: " + str(Inductance))
    L0 = N**2 / Rg0
    print("L0: " + str(L0))
    L1 = N**2 / Rg1
    print("L1: " + str(L1))


p1(3, 101, .37, 10, .15, 20, -7)
p2(234, 0.45, 5, .75, 7)