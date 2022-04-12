import matplotlib.pyplot as plt
import numpy as np

# r = 5
# n = 200
pi = np.pi
data = ""
np.random.seed(0)

def generate(x0, y0, r, n):
    x = []
    y = []
    global data
    for i in range(n):
        angle = np.random.uniform(0, pi * 2)
        radius = r * np.absolute(np.random.randn())
        xx = x0 + radius * np.cos(angle)
        yy = y0 + radius * np.sin(angle)
        x.append(xx)
        y.append(yy)
        data = data + str(xx) + " " + str(yy) + "\n"
    
    return x, y



x, y = generate(0, 0, 5, 200)
plt.plot(x, y, 'bs')

x, y = generate(21, 12, 3, 200)
plt.plot(x, y, 'rs')

x, y = generate(-20, 16, 4, 150)
plt.plot(x, y, 'ks')

with open('./data.txt', 'w') as f:
    f.write(str(data))
    f.close()

plt.show()