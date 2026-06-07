import pandas as pan
import scipy.stats as sst

csf = pan.read_csv("San's  Python Folder/San csv files/products.csv")
# print(csf)

print("\nHead 5 > (0-4) :\n", csf.head())
print("\nBottum 5 > (0-4) :\n", csf.tail())
print("\nInformation :\n", csf.info())
print("\nStatistical Analyse :\n", csf.describe())

print("==> Mean Value")
print(csf.mean)
print("==> Standard Value")
print(csf.std)
print("==> Median Value")
print(csf.median)
print("==> Var Value")
print(csf.var)
# print("\nMax Value :\n")
# print(csf.max())
# print("\nMin Value :\n")
# print(csf.min())

rc = csf

import matplotlib.pyplot as mtpy

bx = rc["Name"]
by = rc["Price"]
mtpy.figure(figsize=(8,8))
mtpy.barh(bx, by, color= ["#e020d0", "#0898f8", "#4ee628", "#fa1212", "#0a07dd", "#584040", "#f8f411", "#044109", "#90c0ec", "#f80764", "#14eff7", "#66A771", "#d1fd0b", "#2E0101", "#3e3caa"])
mtpy.xlabel("Product Price")
# mtpy.ylabel("Product Name")
mtpy.title("Bar Chart - Product csv file")
mtpy.show()

x_stem = by
y_stem = bx
mtpy.figure(figsize= (8,5))
mtpy.stem(x_stem, y_stem, linefmt= "b-", markerfmt= "bo", basefmt = "r-")
mtpy.title("Stem Plot")
mtpy.show()


xpie = bx
ypie = csf.mean
mtpy.pie(ypie, labels=xpie, autopct='%1.1f%%',color= ["#e020d0", "#0898f8", "#4ee628", "#fa1212", "#0a07dd", "#584040", "#f8f411", "#044109", "#90c0ec", "#f80764", "#14eff7", "#66A771", "#d1fd0b", "#2E0101", "#3e3caa"])

