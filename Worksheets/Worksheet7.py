'''
# Question 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
total = 0

while num2 < num1:
    num2 = int(input("The second number must be larger than the first. Try again: "))

for i in range(num1, num2 + 1):
    total += i

print(f"The sum of the numbers between {num1} and {num2} is {total}.")


# Question 2
array = []

# 5 lists
for i in range(5):
    array.append([])
    
    # 5 elements in each list
    for j in range(5):
        array[i].append(5 * i + j)
        
print("[", end="")
for i in range(4):
    print(array[i], ",", sep="")
print(array[4], "]", sep="")


# Question 3
total = 0
for i in range(10):
    num = float(input("Enter a number: "))
    total += num

print(f"The mean is {total / 10} and the total is {total}")
'''


# Question 4
nested_list = [[1, 4, 0, 1, 3, 1], [2, 2, 4, 2, 2, 3], [1, 0, 1, 0, 1, 0]]

# Initialise an empty list to store the moving averages
moving_averages = []

# Loop through each row in the nested list
for i in range(len(nested_list)):
    row_averages = []
    
    # For each row, loop through each element in the row
    for j in range(len(nested_list[i])):
        sum_neighbours = 0
        count_neighbours = 0
        
        # Calculate the top neighbour value if it exists
        if i > 0:
            sum_neighbours += nested_list[i - 1][j]
            count_neighbours += 1
        
        # Calculate the bottom neighbour value if it exists
        if i < len(nested_list) - 1:
            sum_neighbours += nested_list[i + 1][j]
            count_neighbours += 1
        
        # Calculate the left neighbour value if it exist
        if j > 0:
            sum_neighbours += nested_list[i][j - 1]
            count_neighbours += 1
        
        # Calculate the right neighbour value if it exists
        if j < len(nested_list[i]) - 1:
            sum_neighbours += nested_list[i][j + 1]
            count_neighbours += 1
        
        # Calculate the current element value
        sum_neighbours += nested_list[i][j]
        count_neighbours += 1

        # Calculate the mean of the neighbours in total
        mean = sum_neighbours / count_neighbours
        
        # Append the mean to the moving averages list
        row_averages.append(round(mean))
    
    # After all the elements in a row have been processed, append the moving averages list to a new nested list
    moving_averages.append(row_averages)

print(moving_averages)