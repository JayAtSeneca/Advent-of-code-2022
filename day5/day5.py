
import re

def move_crates(stacks, source, dest, num_crates):
    # Move the specified number of crates from the source stack to the destination stack
    for _ in range(num_crates):
    # Remove the top crate from the source stack and add it to the destination stack
        crate = stacks[source].pop()
        stacks[dest].append(crate)
    return stacks


stacks = [['V', 'N','F','S','M','P','H','J'], ['Q', 'D', 'J','M','L','R','S'], ['B','W','S','C''H','D','Q','N'],['L','C','S','R'],['B','F','P','T','V','M'],['C','N','Q','R','T'],['R','V','G'],['R','L','D','P','S','Z','C'],['F','B','P','G','V','J','S','D']]
# stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
steps = []
with open('input.txt') as f:
    for _ in range(10):
        next(f)
    for line in f:
        my_tuple = tuple(map(int,re.findall(r'\d+',line)))
        steps.append(my_tuple)
    print(steps)
    for num_crates, source, dest  in steps:
        source -= 1
        dest -= 1
        stacks = move_crates(stacks, source, dest, num_crates)
    top_crates = [stack[-1] for stack in stacks]
    print(top_crates)