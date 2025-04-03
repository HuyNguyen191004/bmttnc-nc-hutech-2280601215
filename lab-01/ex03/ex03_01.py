def TinhTongChan(list):
    sum=0
    for so in list:
        if so % 2 ==0:
            sum +=so
    return sum

Xuat_list = input("Nhập danh sách các số(các nhau bằng dấu ,): ")
so = list(map(int, Xuat_list.split(',')))

sum_chan =TinhTongChan(so)
print(" Tổng các số chẵn trong list là:",sum_chan)