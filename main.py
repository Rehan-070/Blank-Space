t = int(input())

for _ in range(t):
    n= int(input())
    binary = list(map(int, input().split()))

    ans = 0
    m=0
    # Distance between consecutive gas stations
    for i in binary:
        if i==0:
            m+=1
            ans=max(ans, m)
        else:
            m=0

    print(ans)

