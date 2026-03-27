
input_string = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy : ")
string_list = input_string.split(',')
number_list = []

for s in string_list:    
    clean_s = s.strip()
    if clean_s:
        number_list.append(float(clean_s))

if (len(number_list) == 0):
    print("Danh sách rỗng, không thể tìm số lớn nhất.")

else:
   
    max_value = number_list[0]
      
    for num in number_list:
        if num > max_value:
            max_value = num
    print(f"Số lớn nhất trong dãy là: {max_value}")