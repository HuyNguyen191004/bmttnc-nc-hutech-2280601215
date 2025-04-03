def Tao_tuple_tu_list(lst):
    return tuple(lst)

Xuat_DS = input("Nhập các số vào danh sách(các nha bằng dấu ,): ")
so = list(map(int,Xuat_DS.split(',')))

My_tuple = Tao_tuple_tu_list(so)
print("Danh sách: ",so)
print("Tuple từ danh sách: ",My_tuple)