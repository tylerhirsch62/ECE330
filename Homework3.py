import mymath as math

def p1(V2: int, V1: int, S: float, PF: float) -> None:
    S *= 1000       # power is measured in kVA (in this example)
    # Assuming the transformer is ideal, what would be the magnitude of the current on the primary (200 V) side?
    # S = V1 * I1     ->      V1 * I1 = V2 * I2       ->      I2 = V1 * I1 / V2
    I1 = S / V1
    I2 = V1 * I1 / V2           # I2 = S / V2
    print("I[A] = " + str(I2))

    # Assuming the transformer is ideal, what is the apparent impedance of the load viewed from the primary (200 V) side?
    # V1 = I1 * R1 * PF     ->      R1 = V1 / I1 / PF
    R1 = V1 / I1 / PF
    # V2 = I2 * R2 * PF      ->      R2 = V2 / I2 / PF
    R2 = V2 / I2 / PF
    print("R[ohm] = " + str(R2))

def p2(V2: int, V1: int, S: float, PF: float) -> None:
    S *= 1000       # power is measured in kVA (in this example)
    # Assuming the transformer is ideal, what would be the magnitude of the current on the primary (500 V) side?
    I1 = S / V1
    I2 = V1 * I1 / V2           # I2 = S / V2
    print("I[A] = " + str(I2))

    # Assuming the transformer is ideal, what is the apparent impedance of the load viewed from the primary (550 V) side?
    R2 = V2 / I2 * PF
    X2 = V2 / I2 * math.sin(math.acos(PF))
    print("R[ohm] = " + str(R2))
    print("X[ohm] = " + str(X2))

def p3(i: float, N: int, d: float, g: float) -> None:
    d /= 100    # convert cm to m
    g /= 100    # convert cm to m
    L = 2/100; C = 4/100; R = 2/100
    AL = L*d; AC = C*d; AR = R*d
    mu = 4 * math.pi * 10**(-7)
    RL = g/mu/AL; RC = g/mu/AC; RR = g/mu/AR
    Req = (1 / ((1/RL) + (1/RR))) + RC
    fC = N * i / Req
    fL = fC / 2
    print("Flux through center leg: " + str(fC))
    print("Flux thorugh left leg: " + str(fL))
    print("Flux thorugh right leg: " + str(fL))

def p4(mu: int, N: int, l1: float, l2: float, g: float, flux: float) -> None:
    g /= 100; l1 /= 100; l2 /= 100
    mu = mu * 4 * math.pi * 10**(-7)
    area = (1/100) * (1/100)
    Rc = 2 * (l1 + l2 - (1/100)) / (mu * area) / 10**6
    print(str(Rc))
    mu = 4 * math.pi * 10**-7
    Ra = g / (mu * area) / 10**6
    print(str(Ra))
    i = Rc * flux / N * 10**6
    print(str(i))
    print(361.9301 / i)
    print((l1 + l2) * N)


p4(2000, 108, 10, 5, 0.3, 0.0008)
