from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

eps = 4
min_pts = 2

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

def range_query(x, y, data, eps):
    res = []
    n = len(data)
    for i in range(n):
        if dist(data[i][0] - x, data[i][1] - y) <= eps:
            res.append(i)
    return res

def DBSCAN(data):
    global eps, min_pts
    label = []
    n = len(data)
    for i in range(n):
        label.append(-1)
    C = 0
    for i in range(n):
        if label[i] != -1:
            continue
        N = range_query(data[i][0], data[i][1], data, eps)
        if len(N) < min_pts:
            continue
        label[i] = C
        for item in N:
            if label[item] == -1:
                label[item] = C
            else:
                continue
            _N = range_query(data[item][0], data[item][1], data, eps)
            if len(N) >= min_pts:
                N.extend(_N)
        C += 1
    print(C)
    return label

data = read_file("./data.txt")
label = DBSCAN(data)
style = ['rs', 'bs', 'ks']
n = len(data)
for i in range(n):
    x = data[i][0]
    y = data[i][1]
    k = label[i]
    if k < 0:
        plt.plot(x, y, 'go')
    else:
        plt.plot(x, y, style[k])

plt.show()
        