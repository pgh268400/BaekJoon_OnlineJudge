n = int(input())
def factorial(n):
    if(n == 0):
        return 1
    elif(n <= 2):
        return n
    else:
        return n * factorial(n-1)

result = str(factorial(n))
#print(result)
if(result[-1] != "0"):
    print(0)
else:
    count = 0
    idx = 1
    while True:
        if (str(result)[-1 * idx] != "0"):
            break
        count += 1
        idx += 1
    print(count)