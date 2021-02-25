a = [4, 5, 23, 10, 1, 3, 23, -2, -14]
def solve(a):
    a = sorted(a,reverse = True)
    target = a[0]
    count = 0
    for x in a:
        if x == target:
            count += 1
    return subset(a, count - 1, len(a) - 1, target)

def subset(arr, i, n, s):

    if s == 0:
        return True
    if n == i:
        return False
    if arr[n] <= s:
        return subset(arr, i, n - 1, s - arr[n]) or subset(arr, i, n - 1, s)
    else:
        return subset(arr, i, n - 1, s)    
print(solve(a))




