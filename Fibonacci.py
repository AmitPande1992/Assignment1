a = int(input('Enter number of Fibonaci series'))
num1 = 0
num2 = 1
if a <= 0:
    print("Enter positive integer")

elif a == 1:
    print("Fibonacci series:", num1)

else:
    print("Fibonaci series:")
    for i in range(0,a):
        print(num1)
        i = num1 + num2
        num1 = num2
        num2 = i
