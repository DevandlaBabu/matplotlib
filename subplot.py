import matplotlib.pyplot as plt
import numpy as np 

#Figure = The Entire Canvas
#Ax = A single plot(subplot)📈
x=np.array([1,2,3,4,5])
y=np.array([2,4,6,7,9])
figure,axes = plt.subplots(2,2)

axes[0,0].plot(x,x*2)
axes[0,0].set_title('x*2')

axes[0,1].plot(x,y)
axes[0,1].set_title("xy")

axes[1,0].plot(x,x**2,color="red")
axes[1,0].set_title('x**2')

axes[1,1].plot(x,y**2,color="green")
axes[1,1].set_title('x(y**2)')

plt.tight_layout()





plt.show()