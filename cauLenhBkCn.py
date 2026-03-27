# cau lenh break thuong de trong than cua vong lap
# gap Br se thoat khoi vong lap
# nam trong if de kiem tra dieu kien

# i=0
# while(i<=10):
#     if(i==5):
#         break
#     print("Hoc lap trinh")
#     i+=1
# Hoc lap trinh
# Hoc lap trinh
# Hoc lap trinh
# Hoc lap trinh
# Hoc lap trinh

#nhap vao cac so duong, tinh tong cac so duong vua nhap
# neu gap so am thi thoat, va in ra tong cac so duong vua nhap

# s=0
# while(True): #( vong lap vinh vien, hoac while (1)-vong lap vinh vien)
# # neu de 1 so !=0 trong ngoac thi deu la vong lap vinh vien ( nhung ma co dieu kien dung o trong than vong lap)
#     n= int(input("nhap n="))
#     if(n<0):
#         break
#     s+=n
# print (s)
# nhap n=4
# nhap n=5
# nhap n=6
# nhap n=-1
# 15

# 2- lenh COntinue- khac voi break

# gap ctn no se quay nguoc lai vong lap , thuc hien vong lap tiep theo 
#va khong den duoc lenh sau continue
#break thi se thoat luon
# i=1
# while(i<=10):
#     i += 1
#     print(" Xin chao tat ca cac ban")
#     continue
#     print("to la thanh")

#Tinh tong tat ca cac so chan tu 1-n , voi n nhap tu ban phim
s=0
n=int(input("nhap n="))
for i in range(1,n+1):
    if(i%2==1):
       continue
    s+=i    
    
print(s)