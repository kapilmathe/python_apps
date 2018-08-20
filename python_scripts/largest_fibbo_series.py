# code
def fibbo_series(max_val):
    result = set()
    if max_val < 0:
        return result
    else:
        prev = 0
        curr = 1
        result.add(0)
        i = 1
        while curr <= max_val:
            result.add(curr)
            curr, prev = (curr+prev), curr
            i += 1
        return result

def larget_fibb_seq(l):
    result = list()
    if len(l) == 0:
        return result
    max_val = max(l)
    fs = fibbo_series(max_val)
    for x in l:
        if x in fs:
            result.append(x)
    return result

# print(fibbo_series(7))
T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    res = larget_fibb_seq(l)
    print(" ".join([str(x) for x in res]))