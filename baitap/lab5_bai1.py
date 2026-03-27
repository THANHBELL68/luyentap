#khoi tao danh sach cong viec
task = []
while(True):
    print("\n   CHUONG TRINH CONG VIEC   ")
    print("1. Xem danh sach cong viec")
    print("2. Them cong vec moi")
    print("3. Xoa cong viec ( da hoan thanh)")
    print("0. Thoat")

    choice = input("Moi ban chon chuc nang: ")

    if(choice == '1'):
        if not task:
            print("DANH SACH CONG VIEC RONG !")
        else:
            print("   DANH SACH CONG VIEC   ")
            for i in range (len(task)):
                print(f"{i+1}.{task[i]}")
    
    elif(choice == '2'):
        new_task = input("Nhap ten cong viec moi: ")
        task.append(new_task)
        print(f" Da them cong viec '{new_task}' thanh cong")
    
    elif(choice == '3'):
        task_num_str = input("Nhap so thu tu cong viec muon xoa: ")
        task_num = int(task_num - 1)
        if 1 <= task_num <= len(task):
            removed_task = task.pop(task_num -1)
            print(f"  Da xoa cong viec: '{removed_task}'")
        else:
            print("   So thu tu khong hop le !")

    elif(choice == '0'):
        print("Tam biet")
        break
    else:
        print("Lua chon khong hop le. Vui long ban chon lai.")

