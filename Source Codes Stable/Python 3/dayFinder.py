def month(a):
    m = [0, 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    r = m[a]
    return r


def year(b):
    yy = [0, 6, 4, 2]
    l = (int(b/100))*100
    u = int(l+100)
    k = int(u/100) % 4
    q = yy[k]
    return q


def day(c, m, y):
    dar = ["saturday", "sunday", "monday",
           "tuesday", "wednesday", "thursday", "friday"]
    if ((y % 100)/4) == 0 and (m == 1 or m == 2):
        return(dar[c-1])
    else:
        return(dar[c])


def cal(d, m, y):
    x = d+month(m)+year(y)+(y % 100)+int((y % 100)/4)
    d1 = day(x % 7, m, y)
    return d1


def cheaking(d, m, y):
    n = [1, 3, 5, 7, 8, 10, 12]
    k = [4, 6, 8, 9, 11]
    if (m in n) and d in range(1, 32):
        d2 = cal(d, m, y)
        return d2
    else:
        if (m in k) and d in range(1, 31):
            d2 = cal(d, m, y)
            return d2
        else:
            if m == 2 and (y % 100) % 4 == 0 and d in range(1, 30):
                d2 = cal(d, m, y)
                return d2
            else:
                if m == 2 and d in range(1, 29):
                    d2 = cal(d, m, y)
                    return d2
                else:
                    print("month is not correct")


a = str(input("enter the date in formate DD/MM/YYYY : "))
q = list(map(int, a.split("/")))


d22 = cheaking(q[0], q[1], q[2])
print(d22)
