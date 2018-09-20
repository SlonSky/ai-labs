from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

A = 1
B = 2
C = 3
D = -2
E = 4
F = 7
G = 2
H = 9
K = 3
M = -1
N = 3
P = 2
Q = 4
R = 6
S = 7
V = 5
W = -2
Z = -3

def d12(x, y):
    return A * y + B * x + C

def d13(x, y):
    return D * y + E * x + F

def d23(x, y):
    return G * y + H * x + K

def d1(x, y):
    return M * y + N * x + P

def d2(x, y):
    return Q * y + R * x + S

def d3(x, y):
    return V * y + W * x + Z

zfuncs = [
    d12,
    d13,
    d23,
    # d1,
    # d2,
    # d3
]

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)

for zfunc in zfuncs:
    Z = zfunc(X, Y)

    # Plot the surface.
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
