import array as arr
arr = arr.array('i',[])
n = int(input("nhập số phần tử :" ))
for i in range (n):
    arr.append(int(input('nhập phần tử thứ %d:' %(i+1))))
x = 10
def binary_search(arr, x):
   low = 0
   high = len(arr) - 1
   mid = 0
   while low <= high:
       mid = (high + low) // 2
       if arr[mid] < x:
           low = mid + 1
       elif arr[mid] > x:
           high = mid - 1
       else:
           return mid
   return -1
print(arr,x)
