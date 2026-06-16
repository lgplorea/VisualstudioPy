import pandas as pd
import matplotlib.pyplot as plt
datos = pd.DataFrame({"manzanas": [3, 5], "peras": [6, 2]}, index=["Juan", "Pedro"])
datos.plot.bar()
plt.show()

datos["frutas en total"] = datos["manzanas"] + datos["peras"]
datos.plot.pie(y="frutas en total", autopct="%1.1f%%")
plt.show()