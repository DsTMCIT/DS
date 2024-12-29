import numpy as np
import pandas as pd

url = 'https://github.com/DsTMCIT/DS/raw/refs/heads/main/baseball.csv'
data = pd.read_csv(url, encoding='ms932', sep=',')
print('Data dimension =', data.shape)

height = data.values[:,3]

print('Max =', np.max(height))
print('Min =', np.min(height))
print('Average =', np.mean(height))
print('Variance =', np.var(height,ddof=0))
print('Standard division =', np.std(height,ddof=0))