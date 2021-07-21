#dp는 작은 문제들의 합으로 큰 값을 구한다.
#현재 방식은 재귀로 구성되어 작은문제를 호출하는 Top-Down 방식
#작은 문제들이 반복되므로 메모이 제이션을 활용한다.


#주의 : key값에 value값은 1:1 대응되어야 하며 key값은 변동이 생겨선 안된다.
#튜플만 key값에 들어갈 수 있다. 리스트는 안댐.

memo = {}
def w(a,b,c):
    if (a,b,c) in memo:
        return memo[(a,b,c)]
    if a <= 0 or b <= 0 or c <= 0: #하나라도 0보다 작으면 값은 1
        memo[(0,0,0)] = 1
        return memo[(0,0,0)]
    if a > 20 or b > 20 or c > 20:
        memo[(20,20,20)] = w(20, 20, 20)
        return memo[(20,20,20)]
    if a < b and b < c: #a < b < c
        memo[(a , b , c - 1)] = w(a, b, c-1)
        memo[(a , b - 1 , c - 1)] =  w(a, b-1, c-1)
        memo[(a , b - 1 )] =  w(a, b-1, c)
        return  memo[(a , b , c - 1)] + memo[(a , b - 1 , c - 1)] - memo[(a , b - 1 )]
    #otherwise
    
    memo[(a-1, b , c)] = w(a-1, b, c)
    memo[(a-1, b-1, c)] = w(a-1, b-1, c)
    memo[(a-1, b, c - 1)] = w(a-1, b, c-1)
    memo[(a-1, b-1 , c - 1)] = w(a-1, b-1, c-1)
    return memo[(a-1, b , c)] + memo[(a-1, b-1, c)] + memo[(a-1, b, c - 1)] - memo[(a-1, b-1 , c - 1)]

#매개변수로 넘길땐 이름이 같아도 값만 복사해서 넘긴다. (reference by value)
while True:
    a,b,c = map(int , input().split())
    if(a == -1 and b == -1 and c == -1):
        break
    result = w(a,b,c)
    print(f"w({a}, {b}, {c}) = {result}")