from sys import stdin
input = stdin.readline

result = []

white = 0
blue = 0

def devide(v1, v2, n): #시작행, 시작열, 반복횟수 (몇 곱하기 몇 인지.)
    global white, blue
    total = 0
    for j in range(v1, v1 + n):
        for i in range(v2, v2 + n):
            total += paper[j][i]
            #print(paper[j][i], end= " ")
        #print()

    total_count = n ** 2  #색종이 요소의 개수
    #print("total_count", total_count, "total", total)
    if (total == 0): #전부 흰색이면
        white += 1
        #print("white")
        return False
    elif (total == total_count): #전부 파란색이면
        blue += 1
        #print("blue")
        return False
    
    half = n // 2

#     devide(v1, v2, half)
#     devide(v1 , half , half)
#     devide(half, v2 , half)
#     devide(half, half , half)
    
    devide(v1, v2, half)
    devide(v1 , v2 + half , half)
    devide(v1 + half, v2 , half)
    devide(v1 + half, v2 + half , half)
    
size = int(input().rstrip())
paper = []

for i in range(size):
    data = list(map(int, input().rstrip().split()))
    paper.append(data)
#print(paper)

#paper = [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]

devide(0, 0, size) #우선 전체 탐색.
print(white)
print(blue)