from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt

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

data = read_file("./data.txt")

X = np.array(data)
clustering = AgglomerativeClustering(n_clusters=3, linkage='complete').fit(X)
style = ['rs', 'bs', 'ks']

n = len(data)
for i in range(n):
    x = data[i][0]
    y = data[i][1]
    k = clustering.labels_[i]
    if k < 0:
        plt.plot(x, y, 'go')
    else:
        plt.plot(x, y, style[k])

plt.show()