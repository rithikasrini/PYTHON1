def is_armstrong_number(num):
    
    num_digits = len(str(num))
    
    
    sum_of_cubes = sum([int(digit) ** num_digits for digit in str(num)])
    
    
    return num == sum_of_cubes



lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))


print("The Armstrong numbers are:")
for num in range(lower_range, upper_range + 1):
    if is_armstrong_number(num):
        print(num)
