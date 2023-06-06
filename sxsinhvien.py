class Node:
    def __init__(self, student):
        self.student = student
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
# được sử dụng để chèn một sinh viên mới vào danh sách liên kết.
    def insert(self, student):
        new_node = Node(student)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
# được sử dụng để xuất danh sách sinh viên từ đầu đến cuối danh sách liên kết.
    def display(self):
        current = self.head
        while current:
            print("Tên:", current.student["name"], "- Điểm trung bình:", current.student["Diem_TrungBinh"])
            current = current.next
# sử dụng danh sách liên kết để hoán đổi các sinh viên.
def selection_sort_students(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return

    current = linked_list.head
    while current:
        min_node = current
        next_node = current.next
        while next_node:
            if next_node.student["Diem_TrungBinh"] < min_node.student["Diem_TrungBinh"]:
                min_node = next_node
            next_node = next_node.next
        current.student, min_node.student = min_node.student, current.student
        current = current.next

def main():
    # Tạo danh sách liên kết
    linked_list = LinkedList()

    # Nhập danh sách sinh viên
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        student = {}
        student["name"] = input("Nhập tên sinh viên: ")
        student["Diem_TrungBinh"] = float(input("Nhập điểm trung bình: "))
        linked_list.insert(student)

    # Sắp xếp danh sách sinh viên
    selection_sort_students(linked_list)

    # Xuất danh sách sinh viên đã sắp xếp
    print("Danh sách sinh viên sau khi sắp xếp:")
    linked_list.display()

if __name__ == "__main__":
    main()
