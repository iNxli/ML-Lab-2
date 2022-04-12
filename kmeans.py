import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
eps = 1e-5
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
                
def init(data):
    global k
    n = len(data)
    arr = np.random.randint(0, n + 1, k)
    means = []
    for i in arr:
        means.append(data[i])
    return means

def find_best(xy, means):
    mn = -1
    idx = 0
    i = 0
    for item in means:
        if mn == -1 or (xy[0] - item[0]) ** 2 + (xy[1] - item[1]) ** 2 < mn:
            mn = (xy[0] - item[0]) ** 2 + (xy[1] - item[1]) ** 2
            idx = i
        i += 1
    return idx

def find_center(list):
    xx = 0
    yy = 0
    for xy in list:
        xx += xy[0]
        yy += xy[1]
    xx /= len(list)
    yy /= len(list)
    return xx, yy

def calc_diff(means, new_means):
    res = 0
    n = len(means)
    for i in range(n):
        res += np.sqrt((means[i][0] - new_means[i][0]) ** 2 + (means[i][1] - new_means[i][1]) ** 2)
    return res

def kmeans(data):
    global k, eps
    means = init(data)
    list = []
    for i in range(k):
        list.append([])
    while True:
        for xy in data:
            idx = find_best(xy, means)
            list[idx].append(xy)
        new_means = []
        for i in range(k):
            new_means.append(find_center(list[i]))
        if np.absolute(calc_diff(means, new_means)) < eps * k:
            break
        else:
            means = new_means
    
    return list
            
data = read_file("./data.txt")
means = init(data)
real = [[20.0, 12.0], [0.0, 0.0], [-20.0, 16.0]]
cnt = 0

list = kmeans(data)
style = ['rs', 'bs', 'ks']
for i in range(k):
    for xy in list[i]:
        plt.plot(xy[0], xy[1], style[i])
    xx, yy = find_center(list[i])
    print([xx, yy])
    cnt += calc_diff([[xx, yy]], [real[i]])
    plt.plot(xx, yy, 'yo')

print(cnt / k)

plt.show()