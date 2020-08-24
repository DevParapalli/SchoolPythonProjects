import matplotlib.pyplot as plt
import numpy as np

# arange() --> Return evenly spaced values within a given interval of [a, b)

x = np.arange(-100, 100)
y = x ** 2

plt.plot(x, y, label="y = x ^ 2")
plt.title('15.PythonPyPlot')
plt.grid(True)
plt.legend()
plt.ylim(bottom=0)
plt.show()