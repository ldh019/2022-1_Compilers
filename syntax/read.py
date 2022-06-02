import pandas as pd
import numpy as np
filename = 'table.xlsx'
df = pd.read_excel(filename, engine='openpyxl')
f = open('C:/Users/ldh01/Desktop/2022-1-Compilers/syntax/text.txt', 'w')
print(df)
arr = df.to_numpy()

for i in range(0, 69):
    for j in range(1, 20):
        if type(arr[i][j]) is str:
            string = "\t(" + str(i) + ", '" + str(df.columns[j]) + "'): '" + str(arr[i][j]) + "',\n"
            f.write(string)
