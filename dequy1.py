def  Fibonaci(n):
    f=1
    if n<2:
        f=1
    else:
        f=Fibonaci(n-1) + Fibonaci(n-2)
    return f

n=int(input("nhập n: "))
print(Fibonaci(n))
