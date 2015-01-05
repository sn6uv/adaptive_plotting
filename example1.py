from math import sin, pi
import matplotlib.pyplot as plt

from sampling import sample, resample


def f(t):
    return (t, sin(1/t))

(a, b) = (0.02, 1)
theta = pi / 18.
n = 27
max_depth = 5


plt.figure(1)
plt.subplot(311)
points = sample(f, 2000, a, b)
xs = [point[1][0] for point in points]
ys = [point[1][1] for point in points]
plt.plot(xs, ys, 'k-')

plt.subplot(313)
points = sample(f, n, a, b)
for depth in range(max_depth):
    points = resample(f, points, theta)
xs = [point[1][0] for point in points]
ys = [point[1][1] for point in points]
n = len(points)
plt.plot(xs, ys, 'b-')
plt.plot(xs, [-1.0]*n, 'bd')

plt.subplot(312)
points = sample(f, n-1, a, b)
xs = [point[1][0] for point in points]
ys = [point[1][1] for point in points]
plt.plot(xs, ys, 'r-')
plt.plot(xs, [-1.0]*n, 'rd')

print "total %i points" % n

plt.show()
