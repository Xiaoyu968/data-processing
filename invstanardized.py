import numpy as np
import pandas as pd

# 1. 准备原始数据
# df = pd.read_csv('cao_Tpc_std.csv')
# data = np.array(df['column_name'])
# 2. 设定目标均值和目标方差
target_mean_x1 = 520.8772727272726
target_mean_x2 = 0.9222454545454546
target_mean_x3 = 245.08463636363638
target_mean_y = 730.7436363636364
target_variance_x1 = 4469.834710743802
target_variance_x2 = 0.003204040661157027
target_variance_x3 = 1627.7745140495865
target_variance_y = 5265.658186776861   # 期望方差 (注意：这里设的是方差，计算时需开根号变标准差)

def inv_standardize(data, target_mean, target_variance):
    # 3. 计算原始数据的统计量
    current_mean = np.mean(data)
    current_std = np.std(data, ddof=0) # ddof=0 表示计算总体标准差

    # 4. 执行变换
    # 公式：(x - 旧均值) * (目标标准差 / 旧标准差) + 目标均值
    target_std = np.sqrt(target_variance)
    new_data = (data - current_mean) * (target_std / current_std) + target_mean

    return new_data


# 4. 执行变换
# # 公式：(x - 旧均值) * (目标标准差 / 旧标准差) + 目标均值
# target_std = np.sqrt(target_variance)
# new_data = (data - current_mean) * (target_std / current_std) + target_mean

# # 5. 验证结果
# print(f"原始均值: {current_mean:.2f}, 原始方差: {np.var(data):.2f}")
# print(f"新均值:   {np.mean(new_data):.2f}, 新方差:   {np.var(new_data):.2f}")
# print(f"变换后的数据: {new_data}")