import numpy as np
import matplotlib.pyplot as plt

# Углы в радианах
phi1 = np.deg2rad(24)
phi3 = np.deg2rad(-148)

# Временные интервалы: от -0.02 мс до 0.02 мс → переводим в секунды для расчётов
t_neg_sec = np.linspace(-2e-3, 0, 1000)   # t < 0 (в секундах)
t_pos_sec = np.linspace(0, 2e-3, 1000)    # t >= 0 (в секундах)

# Функции (аргументы в секундах!)
U_c_1 = 1528.81 * np.exp(-14 * t_neg_sec) * np.sin(10000 * t_neg_sec + phi3)  # t < 0
U_c = -2419.096 * np.exp(-13450 * t_pos_sec) + 3921.145 * np.sin(10000 * t_pos_sec + phi1)  # t >= 0
U_pr = 3921.145 * np.sin(10000 * t_pos_sec + phi1)  # t >= 0
U_sv = -2419.096 * np.exp(-13450 * t_pos_sec)  # t >= 0

# Построение графика — ось X в миллисекундах
plt.figure(figsize=(12, 6))

plt.plot(t_neg_sec * 1000, U_c_1, 'm--', linewidth=2, label='U_c1(t), t<0')
plt.plot(t_pos_sec * 1000, U_c, 'r-', linewidth=2, label='U_c(t), t≥0')
plt.plot(t_pos_sec * 1000, U_pr, 'b:', linewidth=2, label='U_pr(t), t≥0')
plt.plot(t_pos_sec * 1000, U_sv, 'g-.', linewidth=2, label='U_sv(t), t≥0')

plt.title('Функция изменения напряжения', fontsize=14)
plt.xlabel('Время t, мс')
plt.ylabel('Напряжение U, В')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
plt.legend(fontsize=10)
plt.xlim(-2, 2)  # ось X уже в мс — задаём пределы напрямую
plt.tight_layout()
plt.show()