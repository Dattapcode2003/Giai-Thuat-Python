# Bài tập 1: Viết chương trình xuất dãy số nguyên ra màn hình
# Bài tập 2: Viết CT tính tổng các số nguyên trong dãy số đã cho. In tổng ra 
n=(int(input()))
import array as arr 
a = arr.array('d',[])
print(a)
for j in range(n):
    a.append(int(input('nhap so thu %d: ' %(j+1))))
print(a)
b=0
for i in range(len(a)):
    b+=a[i]
print("Tổng",b)


