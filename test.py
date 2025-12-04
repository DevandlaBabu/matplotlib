import matplotlib.pyplot as plt

import numpy as np

x = np.array([2023,2024,2025,2026])

y1 = np.array([20,15,30,20])

y2 = np.array([30,12,34,5])

plt.plot(x,y1,marker='.',
             markersize=30,
             markerfacecolor='#32a89b',
             markeredgecolor='blue',
             linestyle="dotted",
             linewidth=3,
             color='black')

line_style=dict(marker='.',
                markersize=30,
                markerfacecolor='#32a89b',
                markeredgecolor='blue',
                linestyle="dotted",
                linewidth=3)
plt.plot(x,y2,color='red',**line_style)

plt.title("class size",fontsize=15,
                       family='Arial',
                       fontweight="bold",
                       color="#1417cd")

plt.xlabel("year",fontsize=15,
                family='Serif',
                fontweight='bold',
                color='#d43368')

plt.ylabel("students",fontsize=15,
                family='Serif',
                fontweight='bold',
                color="#0d91ef76")

plt.xticks(x)

plt.tick_params(axis="both",
                colors='red')
plt.show()
