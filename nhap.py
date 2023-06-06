n = int(input("Nhập giá trị của n: "))
def find_min(arr):
  # Khởi tạo biến min là giá trị đầu tiên của mảng
  min = arr[0]
  # Duyệt qua từng phần tử trong mảng
  for element in arr:
    # Nếu phần tử hiện tại có giá trị nhỏ hơn min, cập nhật lại min
    if element < min:
      min = element
  # Trả về kết quả
  return min
# Test hàm
print(find_min([1, 2, 3, 4])) # Kết quả: 1
print(find_min([-1, 5, -3, 2])) # Kết quả: -3


