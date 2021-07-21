## 최대공약수 - 유클리드 호제법
def gcd(a,b):
    result = 0
    if a < b: #a가 큰수가 아니라면
        #a와 b위치를 바꿔준다. (a가 큰수가 되도록)
        a,b = b,a
    #나머지가 0이 될때까지 반복
    while(b!=0):
        a,b = b, a % b
    return a
        

#최소공배수 구하기 - 유클리드 호제법이용
#예를 들어, X = AB, Y = BC라고 했을 때 X와 Y의 최대공약수는 B, 최소공배수는 ABC임.

def lcm(a,b):
    great = gcd(a,b) #최대공약수를 우선 저장함.
    A = a / great
    B = b / great
    lcm = A * B * great
    return int(lcm)

a,b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))
    