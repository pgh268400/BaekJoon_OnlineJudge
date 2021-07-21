total = 0

n = int(input())

for _ in range(n):
    a = int(input())
    b = int(input())
    #인원수 리스트
    floor = [[i for i in range(1, b+1)]]

    #1층부터 차례대로 만든다.
    people = []
    for i in range(a):
        for j in range(b):
            if(i == 0): #1층이면
                value = floor[i][j]
                people.append(int((value * (value + 1)) / 2))
            else: #2층부터는
                for p in range(j+1): #호수만큼 반복
                    total += floor[i-1][p]
                people.append(total)
        floor.append(people)
        people = []
        total = 0

    print(floor[-1][-1])