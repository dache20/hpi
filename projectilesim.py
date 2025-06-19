import numpy as np
import matplotlib.pyplot as plt

print("projectile simulator thing :)")

try:
    v = float(input("speed? "))
    ang = float(input("angle? "))
    g = float(input("gravity (default 9.81): "))
except:
    print("error in input")
    exit()

a = ang * 3.1416 / 180
vx = v * np.cos(a)
vy = v * np.sin(a)

tmax = (vy*2)/g

T = np.linspace(0, tmax, 89)
X = []
Y = []

for t in T:
    x = vx * t
    y = vy * t - g * t*t / 2
    if y < 0:
        break
    X.append(x)
    Y.append(y)

plt.plot(X, Y)
plt.title("throw arc??")
plt.xlabel("x (meters maybe)")
plt.ylabel("height")
plt.grid(True)
plt.show()
