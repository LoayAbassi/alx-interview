def pascal_triangle(n):
    if n <= 0:
        return []
    l = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if (i > 0 and j > 0 and j < len(l[i-1])):
                row.append(l[i-1][j-1]+l[i-1][j])
            else:
                row.append(1)

        l.append(row)

    return l
