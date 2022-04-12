import numpy as np
import matplotlib.pyplot as plt

INF = 1e9
k = 3

def read_file(str):
    data = []
    with open(str) as f:
        for line in f:
            xy = line.split()
            xy_list = []
            for i in xy:
                i = float(i)
                xy_list.append(i)
            data.append(xy_list)
    return data

def dist(x, y):
    return np.sqrt(x ** 2 + y ** 2)

def calc_dist(i, j, data, point):
    mx = 0
    for p in point[i]:
        for q in point[j]:
            if dist(data[p][0] - data[q][0], data[p][1] - data[q][1]) > mx:
                mx = dist(data[p][0] - data[q][0], data[p][1] - data[q][1])
    return mx

def clink(data):
    global INF, k
    point = []
    n = len(data)
    for i in range(n):
        point.append([i])
    T = n - k
    for t in range(T):
        m = len(point)
        mn = INF
        I = 0
        J = 0
        for i in range(m):
            for j in range(i + 1, m):
                if calc_dist(i, j, data, point) < mn:
                    mn = calc_dist(i, j, data, point)
                    I = i
                    J = j
        point[I].extend(point[J])
        point.pop(J)
    return point

data = read_file("./data.txt")
point = clink(data)
style = ['rs', 'bs', 'ks']
cnt = 0
for p in point:
    for i in p:
        x = data[i][0]
        y = data[i][1]
        plt.plot(x, y, style[cnt])
    cnt += 1

plt.show()