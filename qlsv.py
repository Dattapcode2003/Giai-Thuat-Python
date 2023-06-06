class student:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    n = int(input("Nhập số lượng sinh viên: "))
# Khởi tạo danh sách sinh viên
    students = []
# Nhập thông tin sinh viên
    for i in range(n):
        print(f"\nNhập thông tin sinh viên thứ {i+1}:")
        name = input("Tên sinh viên: ")
        age = int(input("Tuổi sinh viên: "))
        student = {"Tên": name, "Tuổi": age}
        students.append(student)

    # Xuất danh sách sinh viên
    print("\nDanh sách sinh viên:")
    for student in students:
        print(f"Tên: {student['Tên']}, Tuổi: {student['Tuổi']}")
# class SinhVien:
#     def __init__(self, ten, tuoi):
#         self.ten = ten
#         self.tuoi = tuoi

#     def nhap_thong_tin(self):
#         self.ten = input("Nhập tên sinh viên: ")
#         self.tuoi = int(input("Nhập tuổi sinh viên: "))

#     def xuat_thong_tin(self):
#         print(f"Tên sinh viên: {self.ten}")
#         print(f"Tuổi sinh viên: {self.tuoi}")


# Sử dụng lớp SinhVien
sv1 = SinhVien("", 0)
sv2 = SinhVien("", 0)

print("Nhập thông tin sinh viên 1:")
sv1.nhap_thong_tin()

print("\nNhập thông tin sinh viên 2:")
sv2.nhap_thong_tin()

print("\nThông tin sinh viên 3:")
sv1.xuat_thong_tin()

print("\nThông tin sinh viên 4:")
sv2.xuat_thong_tin()