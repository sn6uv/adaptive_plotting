from math import acos, sqrt


def angle(p0, p1):
    return acos((p0[0]*p1[0] + p0[1]*p1[1]) /
                sqrt((p0[0]**2 + p0[1]**2) * (p1[0]**2 + p1[1]**2)))


def sample(f, n, a, b):
    points = []
    for i in range(n+1):
        t = a + i * (b-a) / float(n)
        points.append((t, f(t)))
    return points


def resample(f, points, theta):
    newpoints = []
    for i in range(1, len(points)-1):
        t0, p0 = points[i-1]
        t1, p1 = points[i]
        t2, p2 = points[i+1]
        s0 = 0.5 * (t0 + t1)
        s1 = 0.5 * (t1 + t2)
        v0 = p1[0] - p0[0], p1[1] - p0[1]
        v1 = p2[0] - p1[0], p2[1] - p1[1]
        if angle(v0, v1) > theta:
            if newpoints == [] or abs(s0 - newpoints[-1][0]) > 1e-5:
                newpoints.append((s0, f(s0)))
            newpoints.append((s1, f(s1)))
        elif i == 1:
            newpoints.append((s0, f(s0)))
        elif i == len(points)-2:
            newpoints.append((s1, f(s1)))
    points.extend(newpoints)
    points.sort(key=lambda p: p[0])
    return points
