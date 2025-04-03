def Diem_Lan_Xuat_Hien(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

Xuat_Chuoi = input("Nhập danh sách các từ (cách nhau bằng dấu cách): ")

word_list = Xuat_Chuoi.split()

Xuat_Hien = Diem_Lan_Xuat_Hien(word_list)

print("Số lần xuất hiện của các phần tử: ", Xuat_Hien)