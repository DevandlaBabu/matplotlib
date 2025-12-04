import matplotlib.pyplot as plt
import numpy as np

category=['freshmen','juniors','seniors','lectures']
values=np.array([300,250,275,100])
c=['red','blue','yellow','green']

plt.pie(values,labels=category,
                autopct='%1.1f%%',
                colors=c,
                explode=[0,0,0,0.1],
                shadow=True,
                startangle=90)

plt.title("DataTech institute")
plt.show()