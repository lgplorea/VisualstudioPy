import pandas as pd
import matplotlib.pyplot as plt

# 1. Creamos un conjunto de datos sencillo
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [1500, 2200, 1800, 2500, 3000]
}

# 2. Convertimos los datos en un DataFrame de Pandas
df = pd.DataFrame(data)

# 3. Creamos el gráfico con Matplotlib
plt.figure(figsize=(8, 5))
plt.plot(df['Mes'], df['Ventas'], marker='o', linestyle='-', color='b')

# 4. Personalizamos el gráfico
plt.title('Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas ($)')
plt.grid(True)

# 5. Mostramos el gráfico
plt.show()