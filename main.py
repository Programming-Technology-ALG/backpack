
def brute_force(i: int, ww: int, wc):
    if i < 0:
        return 0
    t = 0
    if wc[i][0] + ww <= m:
        t = brute_force(i - 1, wc[i][0] + ww, wc) + wc[i][1]
    return max(t, brute_force(i - 1, wc[i][0], wc))


def greedy_algorithm(ww: int, mk: int, wc):
    ans = []
    wc = sorted(wc, key=lambda x: x[0] / x[1])
    for j in range(n):
        if wc[j][0] <= mk:
            ww += wc[j][1]  # price
            mk -= wc[j][0]  # weight
            ans.append(wc[j][0])
        else:
            ww += mk * wc[j][1]
            ans.append(wc[j][0])
    return ww


def merge(list1, list2):
    return [(list1[i], list2[i]) for i in range(0, len(list1))]


def discrete_algorithm1(mk: int, wc):
    f = [[0] * mk for k in range(n)]
    for j in range(n):
        for k in range(mk):
            if mk > wc[j][0]:
                f[j][k] = max(f[j - 1][k], f[j - 1][k - wc[j][0]] + c[j])
            else:
                f[j][k] = f[j - 1][k]
    return f[n-1][mk-1]


with open('backpack.txt', "r") as f:
    m, n = next(f).split()
    m = int(m)
    n = int(n)
    k = 0
    for line in f:
        if 0 == k:
            w = list(map(int, list(line.split())))
            k += 1
        if 1 == k:
            c = list(map(int, list(line.split())))
    wc = merge(w, c)
    print(brute_force(n - 1, 0, wc))
    print(greedy_algorithm(0, m, wc))
    print(discrete_algorithm1(m, wc))
