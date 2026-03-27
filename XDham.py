# - la cong thuc duoc chuong trinh xay dung san de thuc hien cong viec tinh toan
#co the xay dung ham dua theo nhu cau cua minh
# tranh viec lap code
# xay dung ham sau do lap gia tri vao .- tiet kiem thoi gian
# tinh toan nhanh hon

# cach xay dung ham
# def ten_ham([<dsthamso]):
#     <ds cac lenh>
#   return ( ket qua tinh gia thua)

def giaithua(a):
    gt=1
    for i in range(1,a+1):
        gt*=i
    return gt # ham ma tra ve gia tri nao do thi phari return
kq=giaithua(5)
# kq=giaithua(5)/(giaithua(3)*giaithua(5-3))
print(kq)

giaithua(5)

#truyen tham so bat buoc
#truyen tham so mac dinh
#truyen tham so la tu khoa
# truyen tham so tuy y
