#1002번 - 터렛 - 두 원의 교점이 곧 마린의 위치다.


def get_case(x1, y1, r1, x2, y2, r2):
    distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if x1 == x2 and y1 == y2 and r1 == r2: #둘이 본 위치와 원이 완전히 겹칠경우
        return -1 #무한대임
    elif distance > (r1 + r2) ** 2: #만나지 않으면
        return 0 #있을 수 없음. (잘못 본것)
    elif distance < (r2 - r1) ** 2: #원이 안에 들어가 있으면
        return 0
    elif distance == (r2 - r1) ** 2: #내접해서 한점에서 만날때
        return 1
    elif distance == (r2 + r1) ** 2: #외접할때
        return 1
    else:
        return 2 #두점에서 만나는경우
    
repeat = int(input())
for i in range(repeat):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) 
    print(get_case(x1, y1, r1, x2, y2, r2))