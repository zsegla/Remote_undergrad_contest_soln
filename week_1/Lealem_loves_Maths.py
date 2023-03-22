#https://codeforces.com/gym/433100/problem/A



# Get the expression from the user
expression = input()

# Split the expression into a list of numbers
numbers = [int(char) for char in expression if char.isdigit()]

# Sort the list of numbers in non-decreasing order
numbers.sort()

# Create a new expression by inserting "+" between the sorted numbers
new_expression = "+".join([str(num) for num in numbers])

# Print the new expression
print(new_expression)
#For example, if the input expression is "2+1+3", the code will output "1+2+3".





