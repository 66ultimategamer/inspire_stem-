# a program that gets the sum of the first 2o numbers

factorial_nums = 1
max_value=int(input("Enter the max value"))
for x in range (1,max_value + 1):
    factorial_nums=factorial_nums + x
    print(factorial_nums)
    
for i in range(0,20,2):
    print(i)

for i in range(0,20,1):
    print(i)