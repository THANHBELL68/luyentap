# # Su dug bien trong python
# #kieu chu
# # s=" Chao cac ban den voi \n TP Hai Duong"
# # print("\"xin chao\"")

# # Toan tu voi chuoi
# # +-*

# # kiem tra 1 chu co o trong chuoi me hay khong?
# s1="hello"
# b="he" in s1
# print(b)

# s="hello cac ban"
# print(s[-1])

# in ra doan con trong chuoi me
# ten bien chuoi
# start( ki tu bat dau)
# end(ki tu cuoi) khong lay = ma lay nho hon
# step (buoc nhay)

#<tenbienchuoi>[<star>:<end>:<step>]
#s="hello cac ban"
#print(s[6:9:1])
#print(s[12:1:-1])

#Thay doi noi dung cua chuoi
#(trong vo ghi)

#in ra gia tri
# %d-so nguyen 9, %f- so thuc 6.8, %s- chuoi-"thanh"
# a=10
# b=20
# print("gia tri cua a la %d va b la %d"%(a,b))

# dung ham format ---de in gia tri ( thamn chieu chi so tu 0)
# a=10
# b=20
# c=10.2
# d="oke em"

# print("gia tri a la{0},b la{1},c la{2},d la {3}".format(a,b,c,d))

s="***hoc lap trinh***"
# print(type(s))
#CAC Phuong THUC
# capitalize()----- Viet hoa chu dau tien trong chuoi
# print(s.capitalize())

#upper()--- chuyen chuoi sang chu in hoa-phuong thuc upper
# print(s.upper())

#lower()-----chuyen chuoi hoa sang chuoi thuong
# print(s.lower())
# khi muon truy cap vao 1 phuong thuc thi nhap bien . phuong thuc do

#title()---chuyen cac ki tu dau moi tu sang in hoa
# print(s.title())

#strip()---- xoa ki tu duoc chi dinh o dau va cuoi moi chuoi
# print(s.strip())

# xoa ki tu chi dinh
# print(s.strip("*"))

#len--- dem so luong ki tu cua mot chuoi
# print(len(s.strip()))
# 
# lstrip()------xoa ki tu duoc chi dinh o ben trai chuoi
# print(s.lstrip("*"))

#split()----tach cac ky tu o trong chuoi
#chuoi.split(char, n)
# vi  du tach doan sau, cu space thi tach, nhap -1 thi tach khong gioi han
s1="xin chao cac ban"
# print(s1.split(" ",-1))
#chi tach xin chao , khong tach cac ban
# print(s1.split(" ",2))
# ==> tao ra 1 mang gom cac phan tu da tach
# print(s1.split())

#count()---- dem so lan xuat hien cua chuoi con trong chuoi goc
s2=" how are you i am huyen"
# print(s2.count("how")) -->1

# s2.count("how",start,end)---dem trong khoang vi tri

#find()-----tim 1 chuoi con trong 1 chuoi goc, neu khong tim duoc thi tra ve -1
# tra ve vi tri chu dau tien tim duoc - 5
# print(s2.find("are"))
# co them doi so giong phuong thuc conut
#s2.find("are",start,end)

#join ---------noi chuoi: 
# ky_tu_noi.join(tham so)
# x = ["hoc","lap","trinh"]
# y="+".join(x) hoc+lap+trinh
# print(y)

# replace()-----Thay the mot chuoi con trong chuoi goc bawng chuoi moi;

t=" xin chao cac ban den voi khoa hoc lap trinh python"
# print(t.replace("khoa"," lop"))--- xin chao cac ban den voi  lop hoc lap trinh python

t2=" xin chao cac ban den voi khoa hoc lap trinh python, day la 1 lop hoc free"
print(t.replace("khoa"," lop",1))