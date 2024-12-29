import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/DsTMCIT/DS/raw/refs/heads/main/baseball_r.csv'
data = pd.read_csv(url, encoding='ms932', sep=',')

df_corr = data.corr(numeric_only=True)

plt.table(cellText=df_corr.values.round(3),
         colLabels=df_corr.columns,
         rowLabels=df_corr.index,
         fontsize=20,
         bbox=[0, 0, 1, 1] )

plt.axis('off')
plt.axis('tight')
plt.show()

