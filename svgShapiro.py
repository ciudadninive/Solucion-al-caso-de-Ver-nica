import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla proporcionada
labels = [
    'Bajo_Pre', 'Bajo_Post', 'Medio_Pre', 'Medio_Post', 'Alto_Pre', 'Alto_Post',
    'Bajo_Pre2', 'Bajo_Post2', 'Medio_Pre2', 'Medio_Post2', 'Alto_Pre2', 'Alto_Post2'
]
shapiro_values = [0.0001, 0.0304, 0.0, 0.0112, 0.0001, 0.0087, 0.0003, 0.0016, 0.0, 0.0093, 0.0033, 0.3326]

# Determinar colores según cumplimiento de normalidad (p > 0.05)
colors = ['green' if p > 0.05 else 'red' for p in shapiro_values]

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(labels, shapiro_values, color=colors)

# Añadir etiquetas de valor encima de cada barra
for bar, value in zip(bars, shapiro_values):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.005, f'{value:.4f}', ha='center', va='bottom')

ax.axhline(0.05, color='black', linestyle='--', label='p = 0.05')
ax.set_xlabel('Grupo')
ax.set_ylabel('Valor p (Shapiro-Wilk)')
ax.set_title('Resultados de prueba Shapiro-Wilk por grupo')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar gráfico en SVG
plt.savefig('shapiro_wilk_results.svg', format='svg')
plt.show()
