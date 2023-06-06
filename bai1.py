
def tinh_tong(n):
    if (n == 1):
        return 1
    return n + tinh_tong(n - 1)
print("Hãy nhập vào số n: ")
n = int(input())
tong = tinh_tong(n);
print("Tổng là: ", tong)
