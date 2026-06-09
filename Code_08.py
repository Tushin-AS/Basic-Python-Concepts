# Logical Operators
# or and not

temp = 25.8
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled.")

temp1 = 34.8
is_sunny = True

if temp1 >= 35 and is_sunny:
    print("It is HOT outside.")
    print("It's sunny.")
elif temp1 <= 20 and is_sunny:
    print("It is COLD outside.")
    print("It's sunny.")
elif 35 > temp1 > 20 and is_sunny:
    print("It is WARM outside.")
    print("It's sunny.")
elif temp1 >= 35 and not is_sunny:
    print("It is HOT outside.")
    print("It's not sunny.")