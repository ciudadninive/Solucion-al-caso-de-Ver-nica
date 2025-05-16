import matplotlib.pyplot as plt

labels = [
    'Bajo_Pre', 'Bajo_Post', 'Medio_Pre', 'Medio_Post', 'Alto_Pre', 'Alto_Post',
    'Bajo_Pre2', 'Bajo_Post2', 'Medio_Pre2', 'Medio_Post2', 'Alto_Pre2', 'Alto_Post2'
]
ks_values = [0.0426, 0.73, 0.0074, 0.2215, 0.0324, 0.3088, 0.0942, 0.0672, 0.062, 0.5462, 0.3429, 0.7813]

# Determinar colores según cumplimiento de normalidad (p > 0.05)
colors = ['green' if p > 0.05 else 'red' for p in ks_values]

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(labels, ks_values, color=colors)

# Etiquetas de valor sobre cada barra
for bar, value in zip(bars, ks_values):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.02, f'{value:.4f}', ha='center', va='bottom')

ax.axhline(0.05, color='black', linestyle='--', label='p = 0.05')
ax.set_xlabel('Grupo')
ax.set_ylabel('Valor p (Kolmogorov-Smirnov)')
ax.set_title('Resultados de prueba Kolmogorov-Smirnov por grupo')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('kolmogorov_smirnov_results.svg', format='svg')
plt.show()
