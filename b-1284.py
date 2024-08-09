while True :
    a = input()
    if a == '0' : break
    res = 0
    for i in a :
        if i == '1' :
            res += 2
        elif i == '0' :
            res += 4
        else :
            res += 3
    print(res + len(a)+1)