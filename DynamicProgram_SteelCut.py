p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24,
     30]  # A sample of a steel bar size and price correspondence,pls be aware that we should start with p[1] neither than p[0]


def cut_recursion(n):  # everage solution
    if n == 0:
        return 0
    q = -100
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_recursion(n - i))
    return q


def buttom_up_cut(n):
    # initial array
    s = [0] * (n + 1)
    r = [0] * (n + 1)

    for j in range(1, n + 1):
        q = -1000
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r[n], s


if __name__ == '__main__':
    i = 7
    print(cut_recursion(i))
    print(buttom_up_cut(i))
