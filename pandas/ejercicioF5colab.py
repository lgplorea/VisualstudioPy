import pandas as pd #Para manipulación de datos
import numpy as np #Para cálculos numéricos
import matplotlib.pyplot as plt #Para visualización de datos
from sklearn.linear_model import LinearRegression #Para modelado de regresión lineal
import warnings #Para gestionar advertencias

# Ignorar todas las advertencias
warnings.filterwarnings("ignore")

# Datos que relacionan la experiencia laboral con el salario anual.
# Leer el archivo csv "Salary.csv" y cargar los datos en un dataframe.
# Especificar la ruta exacta del archivo para evitar errores.
df = pd.read_csv(r"C:\Users\Lorea\OneDrive\Desktop\visualstudio\pandas\Salary.csv")

# Mostrar las primeras 6 filas del DataFrame para revisar los datos.
# Si pongo solo "df.head(6)" VS code ejecuta correctamente (internamente) pero no muestra.
# Para visualizarlo en la terminal hay que poner print por delante.
print(df.head(6))

# Crear un gráfico de dispersión con los datos de "YearsExperience" en el eje x y "Salary" en el eje y
plt.scatter(df["YearsExperience"], df["Salary"])

# Agregar etiquetas al eje x y al eje y para mayor claridad
plt.xlabel("Años de experiencia")  # Etiqueta del eje x
plt.ylabel("Salario anual")  # Etiqueta del eje y

# Mostrar el gráfico, verificamos una correlación positiva y lineal.
plt.show()

# Usamos un modelo de regresión lineal simple para analizar datos y realizar predicciones.
# Crear un objeto de modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo utilizando los datos de "YearsExperience" como características y "Salary" como variable objetivo
modelo.fit(df[["YearsExperience"]], df["Salary"])

# Realizar una predicción del salario anual para 15 años de experiencia
prediccion = modelo.predict([[15]])

# Imprimir la predicción
print(f"Predicción del salario anual para 15 años de experiencia: {prediccion}")

# Ahora graficamos nuevamente agregando la linea recta que nos aporta el modelo de predicción
# ...a traves de la cual se proyectan o predicen los nuevos datos.
# Crear un gráfico de dispersión con los datos de "YearsExperience" en el eje x y "Salary" en el eje y
plt.scatter(df["YearsExperience"], df["Salary"])

# Superponer la línea de regresión del modelo en el gráfico
plt.plot(df["YearsExperience"], modelo.predict(df[["YearsExperience"]]), color="red")

# Agregar etiquetas al eje x y al eje y para mayor claridad
plt.xlabel("Años de experiencia")  # Etiqueta del eje x
plt.ylabel("Salario anual")  # Etiqueta del eje y

# Mostrar el gráfico
plt.show()

# Usa una métrica de evaluación como el coeficiente de determinación (R^2).
# Permite medir la calidad de nuestras predicciones.
# Imprimir el coeficiente de determinación R^2 del modelo, que indica cuánta varianza en la variable dependiente (salario) puede ser explicada por la variable independiente (años de experiencia)
print("R^2: {}".format(modelo.score(df[["YearsExperience"]], df['Salary'])))
