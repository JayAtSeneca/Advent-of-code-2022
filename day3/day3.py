# import string
# dict_cases = dict(zip(string.ascii_lowercase, range(1,26)))
# dict_cases2 = dict(zip(string.ascii_uppercase, range(27,53)))
# dict_cases.update(dict_cases2)
# file = open("day3input.txt","r")
# sum = 0
# for line in file:
#     length = len(line)-1
#     half_length = int(length/2)
#     first_compartment = line[0:half_length]
#     second_compartment = line[half_length:]
#     # print(length)
#     # print(half_length)
#     # print(first_compartment)
#     # print(second_compartment)
#     for i in first_compartment:
#         if i in second_compartment:
#             if i in dict_cases:
#                 sum+=dict_cases[i]
#             break
# print(sum)

# Read the input
file = open("day3input.txt","r")

# Initialize the sum of priorities
sum_of_priorities = 0

# Iterate over the lines of input
for line in file:
  # Split the line in half
  first_half = line[:len(line) // 2]
  second_half = line[len(line) // 2:]

  # Iterate over the characters in the first half
  for c in first_half:
    # Check if the character is present in the second half
    if c in second_half:
      # Calculate the character's priority
      if c.isupper():
        priority = ord(c) - ord("A") + 1 + 26
      else:
        priority = ord(c) - ord("a") + 1

      # Add the priority to the sum
      sum_of_priorities += priority

      # Stop iterating over the first half
      break

# Print the sum of priorities
print(sum_of_priorities)
