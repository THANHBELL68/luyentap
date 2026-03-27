#Kieu tu dien DICT
# khi muon luu cau tru du lieu 
# msv:1
# ten: thanh
# que: HD
# nganh;cntt

# cho phep luu 2 gia tri ,chung ta co the nhap vao <key> va <value>

ttsv={"Msv":1,
            "TenSV":"Tran anh Tuan",
            "QueQuan":"HaNoi",
            "Chuyennganh":"CNTT"
}
# khai bao 1 bien kieu tu dien rong
# thongTinsv1={}
# # gan gia tri mac dinh 
# thongTinsv1=dict({
#             "Msv":2,
#             "TenSV":"Tran anh Tuan",
#             "QueQuan":"HaNoi",
#             "Chuyennganh":"CNTT"
# })

# de truy cap vao cap gia tri k-v, thi dung key
# <tenbien>[<key>]
# print(thongTinsv["TenSV"])

#cach 2- <tenbien>.get(<key>)
#print(thongTinsv.get("Msv"))

# in ra tat ca cac gia tri trong dict

#<tenbien>.values()
#print(thongTinsv.values())

# In ra tat ca cac KEY
#<tenbien>.keys()
# print(thongTinsv.keys())

# Duyet qua tat ca cac phan tu trong kieu tu dien
# for i in thongTinsv:
#     print(i,":",thongTinsv[i])
# Msv : 1
# TenSV : Tran anh Tuan
# QueQuan : HaNoi
# Chuyennganh : CNTT

# Nhap gia tri cho kieu tu dien tu ban phim
# ttsv1={}
# n=int(input("nhap n="))
# for i in range(n):
#     keys = input()
#     values=input()
#     ttsv1[keys]= values
# print(ttsv1)


# Xoa 1 phan tu trong kieui tu dien - xoa di theo Key
#<tenbien>.__delitem__(<key>)
ttsv={  "Msv":1,
            "TenSV":"Tran anh Tuan",
            "QueQuan":"HaNoi",
            "Chuyennganh":"CNTT"
}       
# ttsv.__delitem__("QueQuan")
# for i in ttsv:
#     print(i,":",ttsv[i])

# xoa toan bo thong tin cua bien ttsv
#<tenbien>.clear()
ttsv.clear()
print(ttsv)
#----kq--->{}