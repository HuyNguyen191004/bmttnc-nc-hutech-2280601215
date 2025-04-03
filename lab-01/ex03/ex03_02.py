def Dao_list(lst):
    return lst[::-1]

Xuat_DS = input("Nhập các số vào danh sách(các nha bằng dấu ,): ")

so =list(map(int,Xuat_DS.split(',')))
print("Danh sách trước khi đảo ngược: ",Xuat_DS)
DanSachDaoNguoc = Dao_list(so)
print("Danh sách sau khi đảo ngược: ",DanSachDaoNguoc)