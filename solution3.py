t = int(input())

for _ in range(t):
    n = int(input())
    arr = list( map(int ,input().split()))
    arr.sort()
    
    result = True
    
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        
        if diff > 1:
            result = False
            break
    
    if result == True:
        print("YES")
    else:
        print("NO")
        
