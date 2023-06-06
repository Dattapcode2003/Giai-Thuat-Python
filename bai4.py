def Q(a, b):
    if a < b:
        return 0
    else:
        return Q(a-b, b)+1

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Q(", a, ",", b, ") = ", Q(a,b))