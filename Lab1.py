import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\LuyenTap\Labs\Lab1\ITA105_Lab_1.csv")
df.head()
print(df.head(),"\n")

df.shape
print("1-Kich thuoc du lieu : ",df.shape,"(dong,cot)\n")

print("2-Kieu du lieu va gia tri thieu :\n")
print(df.info(),"\n")

print("3-Thong ke so lieu mo ta cac cot so\n")
print(df.describe(),"\n")

print("4-Kiem tra gia tri thieu-Dem so luong NaN theo cot")
print(df.isnull().sum(),"\n")
print("Kiem tra cu the mot cot :")
cols=["ProductID","Price","StockQuantity","Rating"]
for i in cols:
    df.isnull().sum()
    print("Cot",i,"thieu",df[i].isnull().sum())
print("\n")

print("Dien gia tri bang mean/median/mode")
df["Price_mean"] = df["Price"].fillna(df["Price"].mean(),inplace=False)
print(df["Price_mean"],"\n")

df["Rating_median"] = df["Rating"].fillna(df["Rating"].median(),inplace=False)
print(df["Rating_median"],"\n")

df["StockQuantity_mode"] = df["StockQuantity"].fillna(df["StockQuantity"].mode()[0],inplace=True)
print(df["StockQuantity"],"\n")

print("Loại bo dong - dropna")
df_dropped = df.dropna()

print(" Kiem tra va xu ly cac gia tri bat hop ly trong cot Price va StockQuantity")
df[df["Price"]<0]
df = df[df["Price"]>=0]
df = df[df["StockQuantity"] >= 0]

print("Loc cac gia tri khong hop le trong cot Rating")
df = df[(df["Rating"] > 1) & (df["Rating"] <= 5)]

df["Price_smooth"] = df["Price"].rolling(3).mean()

plt.plot(df["Price"], label="Original Price")
plt.plot(df["Price_smooth"], label = "Smoothed Price")
plt.legend()
plt.show()


df["Category"] = df["Category"].str.lower()

df["Description"] = df["Description"].str.strip()

df["Price_VND"] = df [" Price"] * 26500