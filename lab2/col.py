import numpy as np

def col(p1, p2, m1 = 1, m2 = 1):

    M = m1 + m2
    r1, r2 = p1['r'], p2['r']
    d = np.linalg.norm(r1 - r2)**2
    v1, v2 = p1['v'], p2['v']
    u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
    u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
    return u1, u2
