# sự dụng mảng
def decimal_to_binary_stack(decimal):
    stack = []
    
    while decimal > 0:
        remainder = decimal % 2
        stack.append(remainder)
        decimal //= 2
    binary = 0
    while stack:
        binary = binary * 10 + stack.pop()
    
    return binary

decimal_number = int(input("Nhập số thập phân: "))
binary_number = decimal_to_binary_stack(decimal_number)
print("Số nhị phân tương ứng là:", binary_number)

# Sự dụng dslk đơn
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.top = None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if self.top is None:
#             return None
#         popped_node = self.top
#         self.top = self.top.next
#         return popped_node.data

#     def is_empty(self):
#         return self.top is None


# def decimal_to_binary_stack(decimal):
#     stack = Stack()
    
#     while decimal > 0:
#         remainder = decimal % 2
#         stack.push(remainder)
#         decimal //= 2
    
#     binary = 0
#     while not stack.is_empty():
#         binary = binary * 10 + stack.pop()
    
#     return binary

# decimal_number = int(input("Nhập số thập phân: "))
# binary_number = decimal_to_binary_stack(decimal_number)
# print("Số nhị phân tương ứng là:", binary_number)