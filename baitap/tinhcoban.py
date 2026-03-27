#tinh the tich hinh cau
# v hinh cau = 4/3*pi*r^3
import math as mt
r=float(input(" nhap ban kinh" ))
v= 4/3*mt.pi*mt.pow(r,3)
print("the tich hinh cau la",round(v,2))

# Tinh V lap phuong =a^3
import math as mt
a=float(input(" Nhap vao canh hinh lap phuong"))
v= mt.pow(a,3)
print(round(v,2))

v=round(mt.pow(a,3),2)
print(v)
