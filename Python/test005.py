import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/DsTMCIT/DS/raw/refs/heads/main/baseball.csv'
data = pd.read_csv(url, encoding='ms932', sep=',')
all = data.values
print('all dimension =', all.shape)
height = all[:,3]
weight = all[:,4]

qh25, qh75 = np.percentile(height, [25, 75])
qw25, qw75 = np.percentile(weight, [25, 75])

lower_h = qh25 - ((qh75 - qh25) * 1.5)
upper_h = qh75 + ((qh75 - qh25) * 1.5)
lower_w = qw25 - ((qw75 - qw25) * 1.5)
upper_w = qw75 + ((qw75 - qw25) * 1.5)

r_all=np.array(all)[(data.values[:,3] <= upper_h)
                 & (data.values[:,3] >= lower_h)
                 & (data.values[:,4] <= upper_w)
                 & (data.values[:,4] >= lower_w)]
print('r_all dimension =', r_all.shape)

r_height = r_all[:, 3]
r_weight = r_all[:, 4]

plt.scatter(height, weight, c='blue')
plt.scatter(r_height, r_weight, s=100, c='red', alpha=0.5)
plt.xlabel('height[cm]')
plt.ylabel('weight[kg]')
plt.show()

np.savetxt('baseball_r.csv', r_all, delimiter=',', fmt='%s')
