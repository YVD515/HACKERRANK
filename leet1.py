def twosum(arr, tgt):
    for i in arr:
        for j in range(len(arr)):
            h = i + arr[j]
            while h == tgt:
                p = arr.index(i)
                q = arr.index(arr[j])
                return p, q
arr = [2, 3, 5, 7, 9]
tgt = 12
a, b = twosum(arr, tgt)
print(a, b)

