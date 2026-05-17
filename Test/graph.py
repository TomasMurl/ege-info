import matplotlib.pyplot as plt

# ======================
# Данные для графика 1: Напряжение от тока
# ======================
voltage = [0, 23.118, 38.227, 44.807, 45.398, 42.961, 40.086, 33.383, 31.934, 36.45]
current = [0, 0.4, 0.7, 0.9, 1, 1.08, 1.14, 1.21, 1.24, 1.18]

# Точка при U=45 В (интерполяция)
v_target = 45
for i in range(len(voltage)-1):
    if (voltage[i] <= v_target <= voltage[i+1]) or (voltage[i+1] <= v_target <= voltage[i]):
        v1, v2 = voltage[i], voltage[i+1]
        i1, i2 = current[i], current[i+1]
        i_target_voltage = i1 + (i2 - i1) * (v_target - v1) / (v2 - v1)
        break

# ======================
# Данные для графика 2: Ток от угла
# ======================
angles = [63.947, 62.301, 59.785, 55.49, 50.347, 43.739, 34.736, 23.062, 9.707, -2.711, -16.858, -26.451, -36.327, -42.274, -48.518]

# Повторяем значения тока, чтобы хватило на 15 точек
current_for_angles = current * 2
current_for_angles = current_for_angles[:len(angles)]

# Поиск тока при угле 0 градусов (интерполяция)
angle_target = 0
# Находим отрезок, где угол пересекает 0
for i in range(len(angles)-1):
    if (angles[i] <= angle_target <= angles[i+1]) or (angles[i+1] <= angle_target <= angles[i]):
        a1, a2 = angles[i], angles[i+1]
        c1, c2 = current_for_angles[i], current_for_angles[i+1]
        current_at_angle0 = c1 + (c2 - c1) * (angle_target - a1) / (a2 - a1)
        break

# ======================
# Построение двух графиков
# ======================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# --- График 1: напряжение от тока ---
ax1.plot(current, voltage, 'o-', label='U(I)', color='green', linewidth=2, markersize=6)
ax1.scatter([i_target_voltage], [v_target], color='red', s=100, zorder=5,
            label=f'U=45 В → I≈{i_target_voltage:.2f} А')
ax1.set_title('Зависимость напряжения от тока', fontsize=12)
ax1.set_xlabel('Ток (А)', fontsize=10)
ax1.set_ylabel('Напряжение (В)', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(fontsize=9)

# --- График 2: ток от угла ---
ax2.plot(angles, current_for_angles, 'o-', label='I(угол)', color='purple', linewidth=2, markersize=6)
ax2.scatter([angle_target], [current_at_angle0], color='red', s=100, zorder=5,
            label=f'Угол 0° → I ≈ {current_at_angle0:.2f} А')
ax2.set_title('Зависимость тока от угла', fontsize=12)
ax2.set_xlabel('Угол (градусы)', fontsize=10)
ax2.set_ylabel('Ток (А)', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(fontsize=9)

plt.tight_layout()
plt.show()

# Вывод значения в консоль
print(f"При угле 0 градусов сила тока ≈ {current_at_angle0:.3f} А")