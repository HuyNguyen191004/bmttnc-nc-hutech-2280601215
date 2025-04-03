def kiemtrasonguyen(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
so = int(input("Nhập số cần kiểm tra: "))
if kiemtrasonguyen(so):
    print(so,"là số nguyên tố!")
else:
    print(so,"không phải số nguyên tố!!!")