import matplotlib.pyplot as plt
import numpy as np

categarioes=['friuts','vegtables','protiens','dairy','dry_fruits']
values=np.array([15,10,15,10,20])

plt.bar(categarioes,values)
plt.title("Gym Diet")
plt.xlabel("items")
plt.ylabel('quantity')
plt.show()