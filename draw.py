import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_csv('mse_RSRM.csv',header=None)
data = df1.iloc[:, :].values
x = data[:, 0]
y = data[:, 1]

df2 = pd.read_csv('shenhua_Tpc.csv', header=None)
data2 = df2.iloc[:, :].values
y2 = data2[:, 3]


plt.figure(figsize=(8, 6)) # 设置画布大小

# plt.plot(x, y)
plt.xlabel('Temperature', fontsize=12)
plt.ylabel('Critical Pressure', fontsize=12)
plt.title('Coal Tdep Data', fontsize=14)
plt.scatter(x, y, color='red', s=20, marker='o', alpha=0.7)
plt.scatter(x, y2, color='blue', s=20, marker='x', alpha=0.7)
plt.legend(['RSRM', 'True'], fontsize=10)
# scatter = plt.scatter(x, y, c=colors, cmap='viridis', alpha=0.7)
# plt.colorbar(scatter, label='color intensity')

plt.savefig('mse_SC_T.png',dpi=300, bbox_inches='tight')