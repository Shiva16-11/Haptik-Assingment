a = [4, -5, 23, 10, 1, 3, 23, -2, -14]
def solve(a):
    a = sorted(a,reverse = True)
    target = a[0]
    count = 0
    for x in a:
        if x == target:
            count += 1
    return subset(a, count - 1, len(a) - 1, target)

def subset(arr, startIndex, lastIndex, s):

    if s == 0:
        return True
    if lastIndex == startIndex:
        return False
    if arr[lastIndex] <= s:
        return subset(arr, startIndex, lastIndex - 1, s - arr[lastIndex]) or subset(arr, startIndex, lastIndex - 1, s)
    else:
        return subset(arr, startIndex, lastIndex - 1, s)    
print(solve(a))




