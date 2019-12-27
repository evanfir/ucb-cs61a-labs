def p(num, power):
    if power == 0:
        return 1
    if power == 1:
        return num
    elif power % 2:
        return num * p(num, power - 1)
    else:
        return p(num * num, power // 2)

#        return num * p(num, power - 1)
