import random

#Random Whole Numbers Within a Range
rand_num = random.randint(1,10)
print(rand_num)

# You can generate a random number between 0.0 (inclusive)
# and 1.0 (not inclusive) using the following code from the random module:
rand_num_0_to_1 = random.random()*5
print(rand_num_0_to_1)

# Another way to generate random floating point numbers is to
# use the uniform() function.
random_float = random.uniform(1, 10)
print(random_float)

#Heads or Tails
random_number = random.randint(1,3)
print(random_number)
if random_number == 1:
    print("Heads")
else:
    print("Tails")
