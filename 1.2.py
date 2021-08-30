summary = 0
for cub in range(1, 1000):
    if cub % 2 != 0:
        i = 0
        summa = 0
        cub = str(cub**3+17)
        while i < len(str(cub)):
            summa += int(cub[i])
            i += 1
        if summa % 7 == 0:
            summary += (int(cub))
print(summary)
