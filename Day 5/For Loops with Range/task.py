# The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers
for number in range(1, 11):
    print(number)

# Where the range of numbers is inclusive of the lower bound but not inclusive of the upper bound.
#
# PAUSE 1 - The Gauss Challenge
Total = 0
for num in range (1,101):
    Total += num

print(Total)
