n = int(input())
k = int(input())
cnt = 0
live = [i for i in range(1, n + 1)]
print(live)
while len(live) != 1:
    if k == 1:
        print(n)
        break
    cnt += 1
    if cnt == k:
        del live[cnt]
        cnt = 0
        
    

print(live)
