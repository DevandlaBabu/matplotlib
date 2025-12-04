import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('/Users/devandlababu/Desktop/sd.csv')

math_score = df['math score'].value_counts(ascending=True)

plt.barh(math_score.index,math_score.values,color='red',
                                        edgecolor='black')

plt.title('# of students in maths')
plt.xlabel('marks')
plt.ylabel('# of students')

plt.tight_layout()
plt.show()