import numpy as np
import matplotlib.pyplot as plt

# Datos de las tres pruebas
niveles = [
    {
        "nombre": "Alto",
        "n": 8,
        "W": 0,
        "Wc": 3,
        "p": 0.00781
    },
    {
        "nombre": "Medio",
        "n": 18,
        "W": 14,
        "Wc": 29,
        "p": 0.00597
    },
    {
        "nombre": "Bajo",
        "n": 25,
        "W": 0,
        "Wc": 89,
        "p": 0.00001
    }
]

# Función para graficar cada caso
def plot_wilcoxon(nivel, filename):
    fig, ax = plt.subplots(figsize=(8, 4))

    # Eje X: valores posibles de W
    x = np.linspace(0, nivel["Wc"]*2, 1000)
    # Aproximación de la distribución de Wilcoxon como normal para visualización
    mu = nivel["n"] * (nivel["n"] + 1) / 4
    sigma = np.sqrt(nivel["n"] * (nivel["n"] + 1) * (2*nivel["n"] + 1) / 24)
    y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu)/sigma)**2)

    # Zonas de rechazo y aceptación
    ax.fill_between(x, 0, y, where=(x <= nivel["Wc"]), color="#ffcccc", label="Zona de rechazo")
    ax.fill_between(x, 0, y, where=(x > nivel["Wc"]), color="#ccffcc", label="Zona de aceptación")

    # Curva de distribución
    ax.plot(x, y, color="black", linewidth=2, label="Distribución Wilcoxon (aprox.)")

    # Valor crítico
    ax.axvline(nivel["Wc"], color="red", linestyle="--", linewidth=2, label=f"Wc = {nivel['Wc']}")
    ax.text(nivel["Wc"]+0.5, max(y)*0.8, f"Wc = {nivel['Wc']}", color="red", fontsize=12, rotation=90, va='bottom')

    # Valor observado
    ax.axvline(nivel["W"], color="blue", linestyle="-", linewidth=2, label=f"W = {nivel['W']}")
    ax.text(nivel["W"]+0.5, max(y)*0.6, f"W = {nivel['W']}", color="blue", fontsize=12, rotation=90, va='bottom')

    # Títulos y etiquetas
    ax.set_title(f"Prueba de Wilcoxon - Nivel {nivel['nombre']}\n(n={nivel['n']}, p={nivel['p']})", fontsize=15)
    ax.set_xlabel("Estadístico W")
    ax.set_ylabel("Probabilidad (aprox.)")
    ax.legend(loc="upper right")
    ax.set_xlim(0, nivel["Wc"]*2)
    ax.set_ylim(0, max(y)*1.1)
    plt.tight_layout()
    plt.savefig(filename, format="svg")
    plt.close()

# Generar las tres imágenes
for nivel in niveles:
    plot_wilcoxon(nivel, f"wilcoxon_{nivel['nombre'].lower()}.svg")

print("SVGs generados: wilcoxon_alto.svg, will")
