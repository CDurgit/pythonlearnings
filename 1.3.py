for i in range(1, 101):
    if i == 1:
        print(f'{i} процент')
    elif i > 20:
        i = str(i)
        if int((i[1])) == 1:
            print(f'{i} процент')
        elif 1 < int((i[1])) < 5:
            print(f'{i} процента')
        else:
            print(f'{i} процентов')
    elif 1 < i < 5:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
