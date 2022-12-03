file = open("day1input.txt", "r")
arr = []
i = 0
for line in file:
    if line != "\n":
        i += int(line)
    else:
        arr.append(i)
        i = 0
arr.sort()
print(arr[len(arr) - 1])
print(arr[len(arr)-1] + arr[len(arr)-2] + arr[len(arr)-3])