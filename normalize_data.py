import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv('shenhua_Tpc.csv', header=None)
data = df.iloc[:, :].values
x1 = data[:, 0]
x2 = data[:, 1]
x3 = data[:, 2]
y = data[:, 3]

def find_duplicates_with_indices(nums):
    # 创建一个字典，用于存储 {数值: [索引列表]}
    idx = []
    indices_map = {}
    
    # 遍历列表，记录每个数值出现的所有索引
    for index, value in enumerate(nums):
        if value in indices_map:
            indices_map[value].append(index)
        else:
            indices_map[value] = [index]
    
    duplicates = {val: idxs for val, idxs in indices_map.items()}        
    return duplicates
# print("x中的重复值及其索引:", find_duplicates_with_indices(x))

# x_deduplicate = []
# indices_map = {}
# for index, value in enumerate(x):
#     if value in indices_map:
#         x_deduplicate.append((value+0.001*len(indices_map[value])))
#         indices_map[value].append(index)
#     else:
#         indices_map[value] = [index]
#         x_deduplicate.append(value)
# x_sort = np.sort(x_deduplicate)
# x_idx = {value: index for index, value in enumerate(x_deduplicate)}
# y_sort = [y[x_idx[value]] for value in x_sort]

# df_sorted = pd.DataFrame({'x': x_sort, 'y': y_sort})
# df_sorted.to_csv('methane_sorted.csv', index=False, header=False)
scaler = StandardScaler()

standardized_data = scaler.fit_transform(np.column_stack([x1, x2, x3, y]))
# standardized_data = scaler.fit_transform(np.column_stack([x_sort, y_sort]))

# print("标准化后数据:", standardized_data.flatten())
print("标准化前的均值:", np.mean(x1), np.mean(x2), np.mean(x3), np.mean(y))
print("标准化前的方差:", np.var(x1), np.var(x2), np.var(x3), np.var(y))
print("标准化后均值:", np.mean(standardized_data[:, 0]), np.mean(standardized_data[:, 1]), np.mean(standardized_data[:, 2]), np.mean(standardized_data[:, 3]))
print("标准化后方差:", np.var(standardized_data[:, 0]), np.var(standardized_data[:, 1]), np.var(standardized_data[:, 2]), np.var(standardized_data[:, 3]))
df_standardized = pd.DataFrame(standardized_data)
df_standardized.to_csv('SC_Tpc_std.csv', index=False, header=False)