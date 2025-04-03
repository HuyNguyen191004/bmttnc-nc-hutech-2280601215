def Truy_Cuu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element,last_element

Xuat_tuple = eval(input("Nhập tuple,(ví dụ 1,2,3,4...): "))
first,last = Truy_Cuu(Xuat_tuple)

print("Phần tử đầu: ",first)
print("Phần tử cuối: ",last)