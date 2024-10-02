
# *** basic program ***
# * generate 1 million random numbers,
# ** output should be unique numbers
# *** mark which are prime and non-prime
# *** list repetitive numbers, with the count

import random
from random import sample
# Generate 1000 unique random numbers
random_numbers= random.sample (range (1, 1000000), 100)
# Generate 1000 random number
# random_numbers =[random.randint(1, 1000) for i in range(1000)]
# Print the generated numbers
print(random_numbers)
#Separate even and odd numbers
even_numbers =[num for num in random_numbers if num % 2 ==0]

odd_numbers =[num for num in random_numbers if num % 2 != 0]
#Print even and odd numtiers
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
#Print count of even and odd numbers
print("Count of even numbers:", len(even_numbers))
print("Count of odd numbers:", len(odd_numbers))
# Print count of repeated random numbers
repeated_numbers= [num for num in random_numbers if random_numbers.count(num) > 1]
print("Count of repeated numbers:", len(repeated_numbers))