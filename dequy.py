def Giaithua(n):
    gt=1
    if n==1:
        gt=1
    else:
        gt=n*Giaithua(n-1)
    return gt
a=int(input("nhập a: "))
print(Giaithua(a))
