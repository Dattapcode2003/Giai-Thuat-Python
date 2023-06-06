def tinh_chan(n):
    if (n == 1):
        return 2
    return 2*n + tinh_chan(n - 1)
print("Hãy nhập vào số n: ")
n = int(input())
tong = tinh_tong(n);
print("Tổng là: ", tong)