def Delete(danhsach, key):
    if key in danhsach:
        del danhsach[key]
        return True
    else:
        return False
    
DanhSach = {'a':1,'b':2,'c':3,'d':4}
TuKhoaCanXoa = 'b'
result = Delete(DanhSach, TuKhoaCanXoa)
if result:
    print("Từ đã được xoá khỏi danh sách: ",DanhSach)
else:
    print("Không tìm thấy phần tử trong danh sách.")