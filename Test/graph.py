import matplotlib.pyplot as plt

# Данные
voltage = [63.947, 62.301, 59.785, 55.49, 50.347, 43.739, 34.736, 23.062, 9.707, -2.71]
current = [0, 0.4, 0.7, 0.9, 1, 1.08, 1.14, 1.21, 1.24, 1.28]

# Цель: найти точку, где напряжение = 45 В
v_target = 0

# Интерполяция для нахождения тока при напряжении 45 В
for i in range(len(voltage)-1):
    if (voltage[i] <= v_target <= voltage[i+1]) or (voltage[i+1] <= v_target <= voltage[i]):
        v1, v2 = voltage[i], voltage[i+1]
        i1, i2 = current[i], current[i+1]
        # Линейная интерполяция по напряжению, чтобы найти ток
        i_target = i1 + (i2 - i1) * (v_target - v1) / (v2 - v1)
        break

# Построение графика: напряжение (Y) от тока (X)
plt.figure(figsize=(8, 5))
plt.plot(current, voltage, 'o-', label='U(I) зависимость', color='green', linewidth=2, markersize=6)
plt.scatter([i_target], [v_target], color='red', s=100, zorder=5,
            label=f'Точка при U = {v_target} В\nI ≈ {i_target:.2f} А')

# Оформление
plt.title('График зависимости напряжения от тока', fontsize=14)
plt.xlabel('Ток (А)', fontsize=12)
plt.ylabel('Напряжение (В)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.tight_layout()

plt.show()