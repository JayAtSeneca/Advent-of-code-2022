# Read the input
file = open("day3input.txt","r")
content = file.readlines()
# Initialize the sum of priorities
sum_of_priorities = 0

# Iterate over the lines of input
for i in range(0, 300, 3):
  # Compare each line with the next two lines
  first_line = content[i]
  second_line = content[i + 1]
  third_line = content[i + 2]

  # Iterate over the characters in the first line
  for c in first_line:
    # Check if the character is present in the second and third lines
    if c in second_line and c in third_line:
      # Calculate the character's priority
      if c.isupper():
        priority = ord(c) - ord("A") + 1 + 26
      else:
        priority = ord(c) - ord("a") + 1

      # Add the priority to the sum
      sum_of_priorities += priority

      # Stop iterating over the first line
      break

# Print the sum of priorities
print(sum_of_priorities)
