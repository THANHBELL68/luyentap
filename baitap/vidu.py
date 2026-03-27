d=[]
n=int(input("so sinh vien : "))
for i in range(n):
    d2={"Ms":"","Ten":"","lop":""}
    for j in d2:
        print("nhap",j)
        gt=input()
        d2[j]=gt
    d.append(d2)

for i in range(n):
    print("thong tin sinh vien",i+1)
    print("Ms",d[i]["Ms"],"Ten",d[i]["Ten"],"lop",d[i]["lop"])