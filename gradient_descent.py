import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def linear_regression(x, y, iters = 1000, learning_rate = 0.01):
    n = len(x)
    w = 0
    b = 0
    for it in range(iters):
        y_pr = w * x + b
        dw = -2 / n * np.sum(x * (y - y_pr))
        db = -2 / n * np.sum(y - y_pr)
        w = w - learning_rate * dw
        b = b - learning_rate * db
    return w, b


if os.stat("points").st_size == 0:
    print("points file empty")
    sys.exit()

points = np.loadtxt("points")
x = points[:, 0]
y = points[:, 1]

w, b = linear_regression(x, y, iters = 1000, learning_rate = 0.01)

plt.plot(x, y, 'o')
plt.plot(x, w * x + b)
plt.show()