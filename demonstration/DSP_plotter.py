import numpy as np

N = 8
tap = 8

real_coeff=(1/tap)

def todecimal(x, bits):
    assert len(x) <= bits
    n = int(x,2)
    s = 1 << (bits - 1)
    return (n & s - 1) - (n & s)

# bit repre of coef
coeff_bit= np.binary_repr(int(real_coeff*(2**(N-1))),N)

# double check, invert, should be equal to real coff
todecimal(coeff_bit, N)/(2**(N-1))

# generate time sequence
timeVector = np.linspace(0, 2*np.pi, 100)

output = np.sin(2*timeVector)+np.cos(3*timeVector)+0.3*np.random.randn(len(timeVector))