# Question 1


my_nums = ((5, 10, 15, 20), (2, 4, 6, 8), (57, 68, 79, 81), (1, 3, 5, 7))
final_tuple = [0, 0, 0, 0]

# Loop through the tuple
for i in my_nums:
    # Convert tuple to list and assign it a variable
    temp = list(i)
    
    # Loop throught the list and sum all the elements in the same position    
    for j in range(len(temp)):
        final_tuple[j] += temp[j]

# Convert back to a tuple
final_tuple = tuple(final_tuple)
print(final_tuple)