def tinh_le(n):
    if (n == 1):
        return 1
    return (n*2-1) + tinh_le(n - 1)
print("Hãy nhập vào số n: ")
n = int(input())
tong = tinh_le(n);
print("Tổng là: ", tong)