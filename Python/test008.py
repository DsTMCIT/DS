import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/DsTMCIT/DS/raw/refs/heads/main/baseball_r.csv'
data = pd.read_csv(url, encoding='ms932', sep=',')
all = data.values
height = all[:,3]
weight = all[:,4]

corr = np.corrcoef(height.astype(float), weight.astype(float))[1,0]

fit = np.polyfit(height.astype(float), weight.astype(float), 1)
print('Gradient = {:.4f}'.format(fit[0]))
print('Intercept = {:.4f}'.format(fit[1]))

func = np.poly1d(fit)
xp = np.linspace(np.max(height), np.min(height), 100)
yp = func(xp)

plt.scatter(height, weight)
plt.plot(xp, yp, '-r')

plt.xlabel('height[cm]')
plt.ylabel('weight[kg]')
plt.title('Correlation value={:.2f}'.format(corr))
plt.show()

for i in range(1, len(height)):
    pweight=fit[0]*height+fit[1]
rmse = np.sqrt(np.mean(np.square(weight - pweight)))
print('RMSE = {:.4f}'.format(rmse))

