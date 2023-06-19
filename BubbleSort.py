import array as arr
arr = arr.array('i',[])
n=int(input(' so luong phan tu  :   '))
for j in range(n):
    arr.append(int(input('nhap so thu %d: ' %(j+1))))
print(arr)
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

bubbleSort(arr)
print("xuất mảng ",arr)
