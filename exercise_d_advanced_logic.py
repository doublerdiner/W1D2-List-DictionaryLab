# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
previous_large = 0
previous_small = 100

for num in numbers:
    if num > previous_large:
        previous_large = num
    elif num < previous_small:
        previous_small = num
print(previous_large-previous_small)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
previous_num = 0
for num in numbers:
    if num == previous_num:
        print(True)
    previous_num = num
    
# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


total = 0
waiting_for_7 = False
new_list = numbers.copy()

for num in new_list:
    if num == 6:
        waiting_for_7 = True
    elif num == 7:
        waiting_for_7 = False
    elif waiting_for_7:
        pass
    else: 
        total += num
print(total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

total_2 = 0
previous_num_2 = 0
for num in numbers:
    if num == 13:
        previous_num_2 = 13
        pass
    elif previous_num_2 == 13:
        previous_num_2 = num
        pass
    else:
        total_2 += num
print(total_2)
        





