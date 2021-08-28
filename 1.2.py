cublist = []
sumlist = []
sum_7 = []
for i in range(1, 1001):
    cub = i ** 3
    if cub % 2 == 1:
        # cub += 17   # Добавить что бы решить "+17"
        cublist.append(cub)
for cub in cublist:
    sumop1 = str(cub)
    if len(sumop1) == 1:
        sum = int(sumop1)
        sumlist.append(sum)
    elif len(sumop1) == 2:
        sum = int(sumop1[0]) + int(sumop1[1])
        sumlist.append(sum)
    elif len(sumop1) == 3:
        sum = int(sumop1[0]) + int(sumop1[1]) + int(sumop1[2])
        sumlist.append(sum)
    elif len(sumop1) == 4:
        sum = int(sumop1[0]) + int(sumop1[1]) + int(sumop1[2]) + int(sumop1[3])
        sumlist.append(sum)
    elif len(sumop1) == 5:
        sum = int(sumop1[0]) + int(sumop1[1]) + int(sumop1[2]) + int(sumop1[3]) + int(sumop1[4])
        sumlist.append(sum)
    elif len(sumop1) == 6:
        sum = int(sumop1[0]) + int(sumop1[1]) + int(sumop1[2]) + int(sumop1[3]) + int(sumop1[4]) + int(sumop1[5])
        sumlist.append(sum)
    elif len(sumop1) == 7:
        sum = int(sumop1[0]) + int(sumop1[1]) + int(sumop1[2]) + int(sumop1[3]) + int(sumop1[4]) + int(sumop1[5]) + int \
            (sumop1[6])
        sumlist.append(sum)
    elif len(sumop1) == 8:
        sum = int(sumop1[0]) + int(sumop1[1]) + int(sumop1[2]) + int(sumop1[3]) + int(sumop1[4]) + int(sumop1[5]) + int \
            (sumop1[6]) + int(sumop1[7])
        sumlist.append(sum)
    elif len(sumop1) == 9:
        sum = int(sumop1[0]) + int(sumop1[1]) + int(sumop1[2]) + int(sumop1[3]) + int(sumop1[4]) + int(sumop1[5]) + int \
            (sumop1[6]) + int(sumop1[7]) + int(sumop1[8])
        sumlist.append(sum)
    elif len(sumop1) == 10:
        sum = int(sumop1[0]) + int(sumop1[1]) + int(sumop1[2]) + int(sumop1[3]) + int(sumop1[4]) + int(sumop1[5]) + int \
            (sumop1[6]) + int(sumop1[7]) + int(sumop1[9])
        sumlist.append(sum)
i = 0
for sum in sumlist:
    cub1 = cublist[i]
    i += 1
    if sum % 7 == 0:
        sum_7.append(cub1)
sum = 0
for sumop2 in sum_7:
    sum += sumop2

print(sum)
