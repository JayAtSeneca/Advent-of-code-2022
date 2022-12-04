def count_overlapping_ranges(assignments):
  count = 0
  for assignment1, assignment2 in assignments:
    # Split the assignments into their lower and upper bounds.
    lower1, upper1 = map(int, assignment1.split('-'))
    lower2, upper2 = map(int, assignment2.split('-'))

    # Check if the ranges overlap.
    if upper1 >= lower2 and lower1 <= upper2:
      count += 1

  return count

file = open("day4input.txt","r")
assignments = []
for line in file:
    line = line.replace('\n','')
    tuple_line = tuple(line.split(','))
    assignments.append(tuple_line)
print(count_overlapping_ranges(assignments))
