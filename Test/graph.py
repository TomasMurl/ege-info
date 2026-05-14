import numpy as np
import matplotlib.pyplot as plt

F_1 = [0, 1.1, 3.75, 4.65, 5.1, 5.7, 6.4, 7.35, 7.65, 7.85, 8, 8.33,
       -1.1, -3.75, -4.65, -5.1, -5.7, -6.4, -7.35, -7.65, -7.85, -8, -8.33]

U_12_F_1 = [200, 190, 180, 170, 160, 140, 100, 0, -100, -200, -400,
            -800, 210, 220, 230, 240, 260, 300, 400, 500, 600, 800, 1200]

F_2 = [0, 0.66, 2.25, 2.79, 3.06, 3.42, 3.84, 4.41, 4.59, 4.71, 4.8, 4.998,
        -0.66, -2.25, -2.79, -3.06, -3.42, -3.84, -4.41, -4.59, -4.71, -4.8, -4.998]

U_12_F_2 = [0, 6, 12, 18, 24, 36, 60, 120, 180, 240, 360, 600,
             -6, -12, -18, -24, -36, -60, -120, -180, -240, -360, -600]

F_3 = [0, 0.88, 3, 3.72, 4.08, 4.56, 5.12, 5.88, 6.12, 6.28, 6.4, 6.664,
       -0.88, -3, -3.72, -4.08, -4.56, -5.12, -5.88, -6.12, -6.28, -6.4, -6.664]

U_12_F_3 = [300, 256.986, 164.634, 127.986, 105.662, 70.564, 16.282, -93.958, -183.507,
            -269.873, -434.648, -765.152, 343.014, 435.366, 472.014, 494.338, 529.436, 583.718,
            693.958, 783.507, 869.873, 1034.648, 1365.152]

sort_idx1 = np.argsort(U_12_F_1)
U1_sorted = np.array(U_12_F_1)[sort_idx1]
F1_sorted = np.array(F_1)[sort_idx1]

sort_idx2 = np.argsort(U_12_F_2)
U2_sorted = np.array(U_12_F_2)[sort_idx2]
F2_sorted = np.array(F_2)[sort_idx2]

sort_idx3 = np.argsort(U_12_F_3)
U3_sorted = np.array(U_12_F_3)[sort_idx3]
F3_sorted = np.array(F_3)[sort_idx3]

U_full = np.linspace(min(min(U1_sorted), min(U2_sorted), min(U3_sorted)),
                     max(max(U1_sorted), max(U2_sorted), max(U3_sorted)), 10000)
F1_interp = np.interp(U_full, U1_sorted, F1_sorted)
F2_interp = np.interp(U_full, U2_sorted, F2_sorted)
F3_interp = np.interp(U_full, U3_sorted, F3_sorted)
F_sum = F1_interp + F3_interp

intersection_idx = np.argmin(np.abs(F_sum - F2_interp))
U_cross = U_full[intersection_idx]
F_cross = F2_interp[intersection_idx]
F1_cross = F1_interp[intersection_idx]
F3_cross = F3_interp[intersection_idx]

print(f"Точка пересечения Ф₁+Ф₃ с Ф₂:")
print(f"U₁₂ = {U_cross:.2f}")
print(f"Ф₂ = {F_cross:.4f}")
print(f"Ф₁ = {F1_cross:.4f}")
print(f"Ф₃ = {F3_cross:.4f}")
print(f"Ф₁+Ф₃ = {F1_cross + F3_cross:.4f} (должно равняться Ф₂)")

plt.figure(figsize=(20,7))
plt.plot(U1_sorted, F1_sorted, 'o-', label='Ф₁', linewidth=1.5, markersize=4)
plt.plot(U2_sorted, F2_sorted, 's-', label='Ф₂', linewidth=1.5, markersize=4)
plt.plot(U3_sorted, F3_sorted, '^-', label='Ф₃', linewidth=1.5, markersize=4)
plt.plot(U_full, F_sum, '--', label='Ф₁ + Ф₃', linewidth=2, color='purple')
plt.axvline(x=U_cross, color='red', linestyle=':', alpha=0.7, linewidth=1.5, label=f'U = {U_cross:.1f}')
plt.plot(U_cross, F_cross, 'ro', markersize=8, label=f'Пересечение (U={U_cross:.1f}, Ф={F_cross:.3f})')
plt.plot(U_cross, F1_cross, 'go', markersize=8, label=f'Ф₁ = {F1_cross:.3f}')
plt.plot(U_cross, F3_cross, 'mo', markersize=8, label=f'Ф₃ = {F3_cross:.3f}')
plt.xlabel('U₁₂', fontsize=12)
plt.ylabel('Ф', fontsize=12)
plt.title('Зависимости Ф₁, Ф₂, Ф₃ и Ф₁+Ф₃ от U₁₂', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.figure(figsize=(14,5))
plt.plot(U1_sorted, F1_sorted, 'o-', label='Ф₁', linewidth=2, markersize=5)
plt.plot(U3_sorted, F3_sorted, '^-', label='Ф₃', linewidth=2, markersize=5)
plt.axvline(x=U_cross, color='red', linestyle=':', linewidth=2, alpha=0.8, label=f'U = {U_cross:.1f}')
plt.plot(U_cross, F1_cross, 'go', markersize=10, label=f'Ф₁({U_cross:.1f}) = {F1_cross:.3f}')
plt.plot(U_cross, F3_cross, 'mo', markersize=10, label=f'Ф₃({U_cross:.1f}) = {F3_cross:.3f}')
plt.xlabel('U₁₂', fontsize=12)
plt.ylabel('Ф', fontsize=12)
plt.title('Графики Ф₁ и Ф₃ с вертикальной линией пересечения Ф₁+Ф₃=Ф₂', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()