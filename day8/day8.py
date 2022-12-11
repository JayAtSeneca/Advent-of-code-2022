def count_visible(a, b):
    return next((n+1 for n, x in enumerate(a) if x >= b), len(a))

with open("input.txt") as infile:
    rows=[]
    for line in infile:
        rows.append(list(line.strip()))

    max_score = 0
    visible = 2*(len(rows)-1) + 2*(len(rows[0])-1) 
    for y in range(1, len(rows)-1):
        for x in range(1, len(rows[0])-1):
            elem = rows[y][x]

            if max(rows[y][:x]) < elem or (
                max(rows[y][x+1:]) < elem) or (
                max(rows[yy][x] for yy in range(0,y)) < elem) or (
                max(rows[yy][x] for yy in range(y+1,len(rows))) < elem):
                visible += 1

            score = count_visible(rows[y][x-1::-1], elem)
            score *= count_visible(rows[y][x+1:], elem)
            score *= count_visible([rows[yy][x] for yy in reversed(range(0,y))], elem)
            score *= count_visible([rows[yy][x] for yy in range(y+1,len(rows))], elem)
            max_score = score if max_score < score else max_score

    print (visible, max_score)