"""
Given two integer variables a and b, and a boolean variable flag.
The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.
"""




def CheckFunc(a, b, flag):
    if flag:
        return a < 0 and b < 0  # Both negative
    else:
        return (a >= 0) != (b >= 0)  # Exactly one is non-negative
"""
# Test cases
print(CheckFunc(5, -3, False))   # True
print(CheckFunc(-4, -6, True))   # True
print(CheckFunc(2, 3, False))    # False
print(CheckFunc(-1, -2, False))  # False
"""

# Taking input from user
a = int(input("1st number: "))
b = int(input("2nd number: "))

# Proper way to get boolean input
flag_input = input("Enter boolean value (True/False): ")
flag = flag_input == "true"  # Converts string to actual boolean

print(CheckFunc(a, b, flag))
