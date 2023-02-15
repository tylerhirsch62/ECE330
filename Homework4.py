import mymath as math

def p1(N: int, g: float, d: float, length: float, mu: int, i: float) -> None:
    g /= 100; d /= 100; length /= 100; mu = 4 * math.pi * 10**-7 * mu * 10**6
    area = 3/100 * 1.7/100
    Rc = length / (mu * area)
    print("Relectance of core: " + str(Rc))
    mu2 = 4 * math.pi * 10**-7
    Ra = g / (mu2 * area)
    print("Reluctance of air gap: " + str(Ra))

p1(191, 0.31, 1.7, 40, 1600, 6.7)