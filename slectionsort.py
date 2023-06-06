import array
count = int(input('Nhập số phần tử: '))
A = array.array('i', [])
for i in range(count):
    A.append(int(input('Nhập số {}: '.format(i+1))))

print('Chưa sắp xếp: ', A)
for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

print('Sắp xếp: ', A)

# danh sách lk đơn


