from sys import stdin
input = stdin.readline

ans = 0
N,c,r = map(int, input().rstrip().split())

def recur(N, c, r):
    global ans
    if(N == 0):
        return False
    half = (2 ** N) // 2
    a,b = c // half, r // half
    group = 0
    if((a,b) == (0,0)):
        group = 1
    elif ((a,b) == (0,1)):
        group = 2
    elif ((a,b) == (1,0)):
        group = 3
    elif ((a,b) == (1,1)):
        group = 4
    ans += half * half * (group - 1)
    recur(N-1, c % half, r % half)
recur(N,c,r)
print(ans)