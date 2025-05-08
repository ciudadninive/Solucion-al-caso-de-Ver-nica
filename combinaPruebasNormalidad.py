import pandas as pd
from scipy.stats import shapiro, kstest, norm

# Carga tu archivo Excel y hoja correcta
df = pd.read_excel('BaseDatos.LibroTrabajo.xlsx', sheet_name='MUESTRA')

# Limpia espacios y estandariza los nombres de columna
df.columns = [col.strip() for col in df.columns]

# Define los valores únicos de condición y nivel
condiciones = [1, 2]
niveles = ['Bajo', 'Medio', 'Alto']
momentos = ['Puntaje_Pretest', 'Puntaje_Postest']

resultados = []

for cond in condiciones:
    for nivel in niveles:
        for momento in momentos:
            # Filtra el subgrupo
            sub = df[(df['Condicion_Experimental'] == cond) & (df['NivelLectura-Pretest'] == nivel)]
            datos = sub[momento].dropna()
            # Solo calcular si hay al menos 3 datos
            if len(datos) > 2:
                # Shapiro-Wilk
                shapiro_stat, shapiro_p = shapiro(datos)
                shapiro_result = "Normalidad" if shapiro_p >= 0.05 else "No normalidad"
                # Kolmogorov-Smirnov (ajustando media y std)
                ks_stat, ks_p = kstest(datos, 'norm', args=(datos.mean(), datos.std()))
                ks_result = "Normalidad" if ks_p >= 0.05 else "No normalidad"
            else:
                shapiro_stat = shapiro_p = ks_stat = ks_p = float('nan')
                shapiro_result = ks_result = "Insuficiente N"
            resultados.append({
                'Condicion_Experimental': cond,
                'NivelLectura-Pretest': nivel,
                'Momento': momento,
                'N': len(datos),
                'Shapiro_Wilk_W': round(shapiro_stat, 4) if pd.notnull(shapiro_stat) else '',
                'Shapiro_Wilk_p': round(shapiro_p, 4) if pd.notnull(shapiro_p) else '',
                'Shapiro_Wilk_resultado': shapiro_result,
                'KS_D': round(ks_stat, 4) if pd.notnull(ks_stat) else '',
                'KS_p': round(ks_p, 4) if pd.notnull(ks_p) else '',
                'KS_resultado': ks_result
            })

# Crear DataFrame de resultados
res_df = pd.DataFrame(resultados)
print(res_df)

# Guardar en Excel si lo deseas
res_df.to_excel('Resultados_Normalidad_Explicito.xlsx', index=False)
