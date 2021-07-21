lst = [0,1]
for i in range(2,41):
    lst.append(lst[i-2] + lst[i-1]) #피보나치 수열을 만든다.
    
repeat = int(input())
for _ in range(repeat):
    n = int(input())
    if(n == 0):
        print(1, 0)
    else:
        print(lst[n-1], lst[n])