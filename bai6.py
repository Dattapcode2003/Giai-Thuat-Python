numbers = input("Nhập dãy số nguyên, cách nhau bởi dấu cách: ").split()

# Chuyển đổi các phần tử thành số nguyên
numbers = [int(num) for num in numbers]

# Tìm giá trị nhỏ nhất trong dãy
min_value = numbers[0]  # Giả sử phần tử đầu tiên là nhỏ nhất

for num in numbers:
    if num < min_value:
        min_value = num

print("Giá trị nhỏ nhất:", min_value)