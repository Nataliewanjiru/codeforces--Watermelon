values = input().split()

k,n,m = list(map(int,values))

sum = 0

for i in range(1 , m+1):
    sum += (k*i)

diff = sum - n

if diff < 0 :
    print(0)
else:
    print(diff)
