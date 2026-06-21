import numpy as np
import math

reading = True
while reading:
    f = input("Enter number of points (2-100): ")
    try:
        f = float(f)
        reading = False
    except:
        print("Enter a valid number")

n = math.floor(f)
if n < 2:
    n = 2
if n > 100:
    n = 100

np.random.seed(1)
x = 5 * np.random.rand(n)
w = 5 * np.random.rand()
noise = 5 * np.random.rand(n)
y = w * x + noise

points = np.stack((x, y), axis = 1)
np.savetxt("points", points)
print("Points generated")
