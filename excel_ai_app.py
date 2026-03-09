import pandas as pd
import matplotlib.pyplot as plt

print("Excel AI分析ツール")

file = input("Excelファイル名を入力してください：")

df = pd.read_excel(file)

print("データ概要")
print(df.describe())

df.plot()
plt.show()
