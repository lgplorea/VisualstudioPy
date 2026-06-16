import pandas as pd
import matplotlib.pyplot as plt
datos = pd.DataFrame({"manzanas": [3, 5], "peras": [6, 2]}, index=["Juan", "Pedro"])
datos.plot.bar()
plt.show()