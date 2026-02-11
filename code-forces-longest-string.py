testCases = int(input())

for _ in range(testCases):
    n = input().strip()
    
    if len(n) <= 10:
        print(n)
    else:
        result =[]
        word = list(n)
        result.append(word[0])
        diff = len(n) - 2
        result.append(str(diff))
        result.append(word[-1])
        string = "".join(result)
        print(string)
