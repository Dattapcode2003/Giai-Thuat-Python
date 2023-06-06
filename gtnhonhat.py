n=int(input("Nhập số"))
list=[]
for i in range(n):
    print('phần tử thứ',i,":")
    list.append(int(input()))
print('Số lớn nhất là',max(list))

