import array as arr
m = int(input('Nhập số phần tử: '))
A = arr.array('i', [])
for i in range(m):
    A.append(int(input('Nhập số {}: '.format(i+1))))
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
insertionSort(A)
print('Sắp xếp: ', A)



