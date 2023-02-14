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
    print(i*N/d/g/C)
    print(N*L*d*g/i)

p3(3.5, 234, 2.1, 0.43)
