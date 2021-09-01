import numpy as np
import matplotlib.pyplot as plt

plt.axhline(0, color='red')
plt.axvline(0, color='green')

x = np.arange(-5, 5.0, 0.01)
a = 0 * x
a2 = 0 * x + 2
a3 = 1 * x
a4 = 2 * x
a5 = 2 * x - 5
a6 = x ** 2
a7 = x **2 - 4
a8 = abs(x)
a9 = abs(x) - 5
a10 = abs(x - 5)

plt.plot(x, a)
plt.plot(x, a2)
plt.plot(x, a3)
plt.plot(x, a4)
plt.plot(x, a5)
plt.plot(x, a6)
plt.plot(x, a7)
plt.plot(x, a8)
plt.plot(x, a9)
plt.plot(x, a10)

plt.show()
