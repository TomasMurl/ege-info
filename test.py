import numpy as np
import matplotlib.pyplot as plt

x = float(input("Введите x-координату центра окружности: "))
y = float(input("Введите y-координату центра окружности: "))

theta = np.linspace(0, 2*np.pi, 100)

circle_x = x + 2 * np.cos(theta)
circle_y = y + 2 * np.sin(theta)

plt.plot(circle_x, circle_y)
plt.scatter(x, y, color='red')
plt.grid()
plt.show()