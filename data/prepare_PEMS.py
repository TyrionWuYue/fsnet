import pandas as pd
import numpy as np

data = np.load("E:\DGL\MegaODE\datasets\PEMS04\pems04.npz")['data'][:,:,0]
num_rows = data.shape[0]
num_cols = data.shape[1]

# 创建日期范围，从 2018-01-01 00:00 开始，每行增加 5 分钟
date_range = pd.date_range(start='2018-01-01 00:00', periods=num_rows, freq='5T')

# 创建 DataFrame
df = pd.DataFrame(data, columns=range(num_cols))
df.insert(0, 'date', date_range)

df.to_csv(r"E:\DGL\fsnet\data\PEMS04.csv", index=False)