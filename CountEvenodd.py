list = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0
for i in list:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Odd number is", odd)
print("Even number is", even)

