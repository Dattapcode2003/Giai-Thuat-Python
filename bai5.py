# cách 1
def USCLN(p, q):
    if q == 0:
        return p
    else:
        return USCLN(q, p % q)
q=int(input("Nhập q: "))
p=int(input("Nhập p: "))
print(USCLN(p, q))
#  cách 2 
def USCLN(a,b):
    r=a%b
    if(r==0):
        return b
    else:
        print(a,b,r)
        a=b
        b=r
        return USCLN(a,b)
a=int(input("nhap a:"))
b=int(input("nhap b:"))
print(USCLN(a,b ))