# Conditional expression
# ternary operator
# X if condition else Y

num1 = 5
print("Positive" if num1 > 0 else "Negative")

num2 = 6
result = "Even" if num2 % 2 == 0 else "Odd"
print(result)

a = 25
b = 75
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)