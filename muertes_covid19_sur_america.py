import math
import numpy as np
import matplotlib.pyplot as plt


plt.figure('Muertes covid-19 SA')

paises = ("Colombia", "Venezuela", "Trinidad y Tobago", "Ecuador", "Perú", "Brasil", "Guyana", "Surinam", "Guayana Francesa", "Bolivia", "Paraguay", "Chile", "Argentina", "Uruguay")
posicion_y = np.arange(len(paises))
unidades = (3, 0, 0, 18, 5, 25, 1, 0, 0, 0, 1, 2, 4, 0)

plt.barh(posicion_y, unidades, align = "center")
plt.yticks(posicion_y, paises)
plt.xlabel('Decesos')
plt.title("Decesos por COVID-19 en Sur América")

plt.show()

