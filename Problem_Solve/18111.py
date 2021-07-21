import sys

N, M, B = map(int,  sys.stdin.readline().split())
li = [list(map(int,  sys.stdin.readline().split())) for _ in range(N)]
time, height = 9223372036854775807, 0
for h in range(257): #목표로 하는 높이를 반복함.
    bot = top = 0
    for i in range(N):
        for j in range(M):
            if li[i][j] < h: #목표할 높이보다 작다면
                bot += h - li[i][j] #쌓아야할 높이만큼 저장
            else: #목표할 높이보다 높다면
                top += li[i][j]-h #부숴야할 높이만큼 저장
    if bot > top + B: #쌓아야할 높이 > 부숴서 얻는블럭 + 가지고 있는 블럭 :: 매울 수 없음
        continue #계산하지 않고 현재 h반복문 그냥 넘어감.
    t = bot + top * 2
    if t <= time: #시간 최소값 구함
        time = t
        height = h #h가 iteration 돌고있으므로 가장 높이가 높은게 자동으로 출력됨.
print(time, height)