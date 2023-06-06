# Nhập dãy số nguyên
# tính tổng dãy số nhỏ nhất , lớn nhất , tăg dần, in ra dãy số bé , lớn nhất

n=(int(input()))
import array as arr 
a = arr.array('d',[])
print(a)
for j in range(n):
    a.append(int(input('nhap so thu %d: ' %(j+1))))
print(a)
b=0
c=a[0]
d=a[0]
for i in range(len(a)):
    b+=a[i]
print("Tổng",b)
for i in range(len(a)):
    if c<a[i]:
        c=a[i]
print('so lon nhat la',c)
for l in range(len(a)):
    if d>a[l]:
        d=a[l]
print('so nhỏ nhat la',d)
for u in range(len(a)):
    for o in range(u,len(a)):
        if a[u]>a[o]:
            m=a[u]
            a[u]=a[o]
            a[o]=m
print(a)