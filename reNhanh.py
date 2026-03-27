# cau truc re nhanh if-sap xep bai toan chat che
# xcem loai hoc sinh
# neu dtb<5- y
# neu dtb>=5 va <7 - tb
# neu dtb>=7 va <8 - kha
# neu dtb >=8 va < 9 -- g
# neu dtb>= 9 -- xs

dtb=float(input(" nhap diem trung binh :"))
if(dtb >=0 and dtb <=10):
    if(dtb<5):
        print(" y")
    elif(dtb>=5 and dtb<7):
        print("tb")
    elif(dtb>=7 and dtb<8):
        print("k")
    elif(dtb>=8 and dtb<9):
        print("g")
    else:
        print("xs")
else:
    print(" Moi ban nhap lai diem ")
