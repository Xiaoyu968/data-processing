from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import math
from invstanardized import inv_standardize
df = pd.read_csv('SC_Tpc_std.csv', header=None)
data = df.iloc[:, :].values
x1 = data[:, 0]
x2 = data[:, 1]
x3 = data[:, 2]
y_true = data[:, 3]

df2 = pd.read_csv('shenhua_Tpc.csv', header=None)
data2 = df2.iloc[:, :].values
x4= data2[:, 0]
# # y_true2 = data2[:, 1]
# print(x)
# 定义两组列表（例如：真实值 y_true 和 预测值 y_pred）


def pre(x1, x2):
    y = (3.04*x1 + 0.252*x2**2 + 0.7346*x2 + 0.0892)/(0.36*x2 + 3.77)
    return y

y_true_original = inv_standardize(np.array(y_true), 730.7436363636364, 5265.658186776861)
y_pred_RSRM_Standard = [pre(xi_1, xi_2) for xi_1, xi_2 in zip(x1, x2)]
y_pred = inv_standardize(np.array(y_pred_RSRM_Standard), 730.7436363636364, 5265.658186776861)

# 计算 MSE
mse = mean_squared_error(y_true_original, y_pred)

print(f"MSE (sklearn): {mse}")

df_RSRM = pd.DataFrame({'x': x4, 'y_pred_RSRM': y_pred})
df_RSRM.to_csv('mse_RSRM.csv', index=False, header=False)
