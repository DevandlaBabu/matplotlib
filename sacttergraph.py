import matplotlib.pyplot as plt
import numpy as np

x1=np.array([1,2,2,3,3,4,5,6,6,7])#hours studied
y1=np.array([65,68,70,75,76,80,85,83,90,95])#marks obtainted

x2=np.array([0,1,2,3,4,5,6])#hours studied
y2=np.array([65,68,70,75,76,80,90])#marks obtainted


plt.scatter(x1,y1,color='green',
                alpha=0.5,
                s=200,
                label='class A')


plt.scatter(x2,y2,color='blue',
                alpha=0.7,
                s=100,
                label='class B')


plt.title("marks of student")
plt.xlabel("hours")
plt.ylabel('grades')

plt.legend()
plt.show()