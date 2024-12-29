import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/DsTMCIT/DS/raw/refs/heads/main/baseball.csv'
data = pd.read_csv(url, encoding="ms932", sep=",")
all = data.values
height = all[:,3]
weight = all[:,4]

plt.scatter(height, weight)
plt.xlabel('height[cm]')
plt.ylabel('weight[kg]')

plt.show()
