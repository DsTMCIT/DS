import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/DsTMCIT/DS/raw/refs/heads/main/baseball.csv'
data = pd.read_csv(url, encoding='ms932', sep=',')
all = data.values
height = all[:,3]
weight = all[:,4]

plt.hist(height, 40)
plt.xlim(130, 260)
plt.ylim(0, 120)
plt.xlabel('height[cm]')
plt.ylabel('count')

plt.show()
