import numpy as np
import matplotlib.pyplot as plt

# Параметры
w = 1
t = np.linspace(0, 2*np.pi, 1000)

def deg(x):
    return np.deg2rad(x)

# ===== ПЕРВАЯ ФУНКЦИЯ =====
h1_1 = 110 * np.sin(w*t - deg(11.6))
h1_2 = 105.297 * np.sin(3*w*t + deg(180))
h1_3 = 2.97 * np.sin(5*w*t + deg(72.147))
u1 = h1_1 + h1_2 + h1_3

plt.figure()
plt.plot(t, h1_1, linestyle=':')
plt.plot(t, h1_2, linestyle='-.')
plt.plot(t, h1_3, linestyle='--')
plt.plot(t, u1, linewidth=2)

plt.title("Разложение I функции")
plt.legend(["1-я гармоника", "3-я гармоника", "5-я гармоника", "Сумма"])
plt.grid(True)

# ===== ВТОРАЯ ФУНКЦИЯ =====
h2_1 = 110 * np.sin(w*t - deg(11.6))
h2_2 = 48.79 * np.sin(3*w*t + deg(159))
h2_3 = 2.97 * np.sin(5*w*t + deg(72.147))
u2 = h2_1 + h2_2 + h2_3

plt.figure()
plt.plot(t, h2_1, linestyle=':')
plt.plot(t, h2_2, linestyle='-.')
plt.plot(t, h2_3, linestyle='--')
plt.plot(t, u2, linewidth=2)

plt.title("Разложение II функции")
plt.legend(["1-я гармоника", "3-я гармоника", "5-я гармоника", "Сумма"])
plt.grid(True)

# ===== ТРЕТЬЯ ФУНКЦИЯ =====
h2_1 = 110 * np.sin(w*t - deg(11.6))
h2_2 = 48.79 * np.sin(3*w*t + deg(159))
h2_3 = 2.97 * np.sin(5*w*t + deg(72.147))
u2 = h2_1 + h2_2 + h2_3

plt.figure()
plt.plot(t, h2_1, linestyle=':')
plt.plot(t, h2_2, linestyle='-.')
plt.plot(t, h2_3, linestyle='--')
plt.plot(t, u2, linewidth=2)

plt.title("Разложение III функции")
plt.legend(["1-я гармоника", "3-я гармоника", "5-я гармоника", "Сумма"])
plt.grid(True)

plt.show()