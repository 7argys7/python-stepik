n = int(input())
k = int(input())
live = [i for i in range(1, n + 1)]
new_live = []
while len(live) != 1:
    if k == 1:
        print(n)
        break
    new_live += live[:(k - 1) % len(live)]
    if len(live) < k:
        del live[:k % len(live)]
    else:
        del live[:k] 
    live += new_live
    print(live)
    new_live = []


print(*live)
