def chia_het(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan,2)
    if so_thap_phan % 5 ==0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input("Nhập số nhị phân (phân tách bởi dấu ,): ")
list_so_nhi_phan = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in  list_so_nhi_phan if chia_het(so)]
if len(so_chia_het_cho_5)>0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:",ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi!!!!")