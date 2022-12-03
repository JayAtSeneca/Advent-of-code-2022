#part-1
# file = open("day2Input.txt", "r")
# my_dict = {'X':1, 'Y':2, 'Z':3}
# score = 0
# for line in file:
#     opponent = line[0]
#     you = line[2]
#     score += my_dict[you]
#     if (opponent == 'A' and you == 'X') or (opponent == 'B' and you == 'Y') or (opponent == 'C' and you == 'Z'):
#         score+=3
#     elif (opponent == 'A' and you == 'Y') or(opponent=='B' and you=='Z')or (opponent=='C'and you=='X'):
#         score += 6
#     else:
#         score += 0
# print(score)


#part-2
file = open("day2Input.txt", "r")
dicto = {'X':1, 'Y':2,'Z':3}
my_dict = {'X':0, 'Y':3, 'Z':6}
score = 0
for line in file:
    opponent = line[0]
    you = line[2]
    score += dicto[you]
    #X means you need to lose
    if you == 'X':
        if opponent == 'A':
            you = 'Z'
        elif opponent == 'B':
            you = 'X'
        elif opponent == 'C':
            you = 'Y'
    #Y means you need to end the round in a draw
    elif you == 'Y':
        if opponent == 'A':
            you = 'X'
        elif opponent == 'B':
            you = 'Y'
        elif opponent == 'C':
            you = 'Z'

    #Z means you need to win
    else:
        if opponent == 'A':
            you='Y'
        elif opponent == 'B':
            you = 'Z'
        elif opponent == 'C':
            you = 'X'
    if (opponent == 'A' and you == 'X') or (opponent == 'B' and you == 'Y') or (opponent == 'C' and you == 'Z'):
        score += 3
    elif (opponent == 'A' and you == 'Y') or(opponent=='B' and you=='Z')or (opponent=='C'and you=='X'):
        score += 6
    else:
        score += 0
print(score)