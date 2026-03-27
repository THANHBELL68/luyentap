# muon luiu tru gia tri cung kieu( mang)
#vd tao danh sach diem trung binh
# co the tao ds co nhieu kieu gia tri khac nhau trong py thon

# tb=[6.7, 7.8, 8.9, 5.6]
# print(tb)   
# print(type(tb))
# a=[7, 7.8, "hello"]
# print(a)

# cach 2- dung list()- tao danh sach
# a= list([1,2,3,4,5]) # khai bao va khoi tao luon thi them ngoac [ vafo trong]
# print(a)

# # trong 1 danh sach co the long duoc nhieu danh sach khac vao
# #vd
# a=[[1,2,3],[4,5,6],7,[]]
# print(a)


# a=[8,6,5,9,10,12]
# de truy cap vao phan tu trong ds thi dung chi so
#truy cap xuoi , nguoc(-)
# print(a[1])

# truy cap bang <tendanhsach>[star:end:step]

# print(a[0:3:2])

#Them phan tu vao cuoi danh sach
# <ten_ds>.append() # NOi them phan tu vao cuoi
# a.append(8)
# a.append(9)
# print(a)

#Them phan tu vao Giua danh sach.
#<ten_ds>.insert(vi tri them , GiaTri them)
# a.insert(3,10)
# print(a)

# a=[8,6,5,9,10,12]
#xoa phan tu trong danh sach
# ap dung phuong thuc ._delitem_()
#<ten_ds>.__delitem__(<index>)
#index(chi so phan tu)
# a.__delitem__(3) # co 2 noi _ _
# print(a)

xoa gia tri danh sach
<tends>.remove(<gt_can_xoa>)
a=[8,6,5,9,10,12]
a.remove(8)
print(a)

Nhap vao 1 danh sach tu ban phim
1- khoi tao 1 danh sach rong
a=[]
n=int(input("n="))
# dung vong lap for de lap qua moi phan tu trong danh sach
#moi lan lap thi lai cho nhap vao
for i in range(n): #( lap tu 0-<n)
    print(" nhap phan tu thu" ,i+1,":",end = "")
    x= int(input()) #( cho nguoi dung nhap x)
    a.append(x) # sau khi cu nhap thi tu khac them vao phan tu cua mang
print(a)    
n=6
1
2
3
4
5
6
[1, 2, 3, 4, 5, 6]

#in ra tung gia tri ma nguoi dung nhap vao

# for gt in a: #(a là mang, gt-la gia tri, gt chay qua het cac ptu trong mang)
    # print("Gia tri phan tu cua mang:",gt)

#nhap vao n phan tu vao danh sach va tinh tong cac phan tu
#sum(<ds>)
# lay do daii cua danh sach a -dung len(<ds>)
# tong =sum(a)
# print(len(a))

# sap xep cac phan tu trong mang
# sorted(<ds>)
# b=[9,8,7,6,5,4,3,2,1]
# c= sorted(b)
# print(c)

# Sap xem cac phan tu cua mang khi lon xon
#sorted(<ds>, reverse=True) ( them doi so)
#True-giam dan
#fale- tang dan
b=[1,4,6,8,2,8]
c=sorted(b,reverse=False)
print(c)

#ham max(<ds>)- lay gia tri lon nhat trong ds
#ham min(<ds>)- lay gia tri nho nhat