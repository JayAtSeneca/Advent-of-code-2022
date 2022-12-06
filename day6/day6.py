with open('input.txt') as f:
    string = f.read()
def day_6(x):
    for i in range(len(string)):
        if i >= x-1:
            temp = string[i:i-x:-1]
            unique = []
            for j in temp:
                if j not in unique:
                    unique.append(j)
                else:
                    pass
            if len(unique) == x:
                print(i+1)
                break
#part one
day_6(4)
#part two
day_6(14)