import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/DsTMCIT/DS/raw/refs/heads/main/baseball.csv'
data = pd.read_csv(url, encoding='ms932', sep=',')
all = data.values
height = all[:,3]
weight = all[:,4]

print('Quartile: h25% =', np.percentile(height, 25))
print('Quartile: h50% =', np.percentile(height, 50))
print('Quartile: h75% =', np.percentile(height, 75))
print('Median: Center=', np.median (height))

qh25, qh50, qh75 = np.percentile(height, [25, 50, 75])
print('Q25% = ', qh25, ', Q75% = ', qh75)

plt.boxplot(height)
plt.xlabel('height')
plt.ylabel('[cm]')
plt.show()