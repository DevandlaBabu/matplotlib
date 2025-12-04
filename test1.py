import matplotlib.pyplot as plt
 
import numpy as np

x=[2021,2022,2023,2024,2025]

y=[5,10,15,20,25]

plt.grid(axis="x",
         linewidth=2,
         color="lightgray",
         linestyle="dashed")

plt.plot(x,y)
plt.xticks(x)
plt.show()

