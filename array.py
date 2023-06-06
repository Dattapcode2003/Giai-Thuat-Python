# Ví dụ: Viết chương trình nhập dãy số nguyên
import array as arr 
numbers = arr.array('i',[])
print(numbers)
for j in range(5):
    numbers.append(int(input('nhap so thu %d: ' %(j+1))))
print(numbers)
for i in range(len(numbers)): 
    print(numbers[i])
numbersSum = sum(numbers) 
print('Tổng là',numbersSum)
