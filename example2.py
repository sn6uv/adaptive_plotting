from math import sin, pi
import matplotlib.pyplot as plt

from sampling import sample, resample


def f(t):
    return (t, sin(pi * t * n))

(a, b) = (0, 1)
n = 27
max_depth = 3
theta = pi / 18.

points = sample(f, n, a, b)
for depth in range(max_depth):
    points = resample(f, points, theta)
xs = [point[1][0] for point in points]
ys = [point[1][1] for point in points]
plt.plot(xs, ys, 'bo-')
plt.ylim(-1, 1)
plt.show()
