students = []
n = int(input("Nhập số lượng sinh viên: "))
for i in range(n):
    student = {}
    student['name'] = input("Nhập tên sinh viên thứ %d: " % (i+1))
    student['dob'] = input("Nhập ngày sinh của sinh viên: ")
    student['hometown'] = input("Nhập quê quán của sinh viên: ")
    student['phonenumber'] = input("Nhập số điện thoại của sinh viên: ")
    student['cmnd'] = input("Nhập CMND của sinh viên: ")
    students.append(student)

x = input("Nhập tên sinh viên cần tìm: ")

def binary_search(students, x):
    low = 0
    high = len(students) - 1
    while low <= high:
        mid = (high + low) // 2
        if students[mid]['name'] < x:
            low = mid + 1
        elif students[mid]['name'] > x:
            high = mid - 1
        else:
            return mid
    return -1

result = binary_search(students, x)
if result == -1:
    print("Không tìm thấy sinh viên trong danh sách.")
else:
    student = students[result]
    print("Thông tin sinh viên %s:" % student['name'])
    print("Ngày sinh:", student['dob'])
    print("Quê quán:", student['hometown'])
    print("Số điện Thoại:", student['phonenumber'])
    print("CMND:", student['cmnd'])
