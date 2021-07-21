from sys import stdin
input = stdin.readline

paper = []
minus_one , zero, one = 0,0,0
def recur_cut(row, col, size): #행, 열, 반복크기
    global minus_one, zero, one
    minus_count, zero_count, one_count = 0,0,0
    
    total = 0
    for i in range(row, row+size):
        for j in range(col, col+size):
            if paper[i][j] == 0:
                zero_count += 1
            elif paper[i][j] == 1:
                one_count += 1
            elif paper[i][j] == -1:
                minus_count += 1

    #종이가 모두 같은수로 되어있으면 사용한다. 
    if one_count == (size ** 2):
        one += 1
        return False
    elif minus_count == (size ** 2):
        minus_one += 1
        return False
    elif zero_count == (size ** 2):
        zero += 1
        return False
    
    for i in range(0, 3):
        for j in range(0, 3):
            recur_cut(row + size // 3 * i, col + size // 3 * j, size // 3)
n = int(input().rstrip())
for _ in range(n):
    data = list(map(int , input().rstrip().split()))
    paper.append(data)
    
recur_cut(0,0,n)

print(minus_one)
print(zero)
print(one)