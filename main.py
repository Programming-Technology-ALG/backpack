def brute_force(i: int, ww: int, wc):
    if i < 0:
        return 0
    t = 0
    if ww + wc[i][0] <= m:
        t = brute_force(i - 1, wc[i][0] + ww, wc) + wc[i][1]
    return max(t, brute_force(i - 1, ww, wc))


def greedy_algorithm(ww: int, mk: int, wc):
    for j in range(n):
        if wc[j][0] <= mk:
            ww += wc[j][1]  # price
            mk -= wc[j][0]  # weight
            print(wc[j])
        else:
            ww += mk * wc[j][1] / wc[j][0]
            print(mk, "weight from", wc[j])
            return ww
    return ww


def merge(list1, list2):
    return [(list1[i], list2[i]) for i in range(len(list1))]


def printArr(arr):
    for i in range(n):
        print(arr[i])
    return


def discrete_algorithm1(mk: int, wc):
    a = [[0] * mk for k in range(n)]
    for i in range(n):
        for j in range(mk):
            if i > 0:
                if j - wc[i][0] >= 0:
                    a[i][j] = max(wc[i][1] + a[i - 1][j - wc[i][0]], a[i - 1][j])
                else:
                    a[i][j] = a[i - 1][j]
            elif j >= wc[i][0]:
                a[i][j] = wc[i][1]
    # printArr(a)
    return a[n - 1][m - 1]


with open('backpack.txt', "r") as f:
    n, m = next(f).split()
    m = int(m)
    n = int(n)
    wc = sorted(merge(list(map(int, next(f).split())),
                      list(map(int, next(f).split()))), key=lambda x: x[0] / x[1])
    print("\nTask 1\n", brute_force(n - 1, 0, wc))
    print("\nTask 2"), print("Total coast: ", greedy_algorithm(0, m, wc))
    print("\nTask 3\nTotal coast: ", discrete_algorithm1(m, wc))
