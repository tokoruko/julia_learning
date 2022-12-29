def recur(i):
    if i <= 0 :
        return 0
    else:
        x = i * i
        print(x)
        return recur(i-1)
