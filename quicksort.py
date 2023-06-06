def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Duyệt qua các phần tử từ 0 đến n-i-1
        # Vì sau mỗi lượt, phần tử lớn nhất sẽ được đặt ở cuối, nên không cần duyệt lại
        for j in range(0, n-i-1):
            # So sánh hai phần tử liền kề
            if arr[j] < arr[j+1]:
                # Hoán đổi chúng nếu phần tử bên phải lớn hơn phần tử bên trái
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Dãy số ban đầu
numbers = [9, 15, 3, 12, 22, 7]

# Sắp xếp dãy số bằng phương pháp Bubble Sort
bubble_sort(numbers)

# In kết quả sau khi sắp xếp
print("Kết quả: ", end="")
for number in numbers:
    print(number, end=" ")
