from sys import stdin
input = stdin.readline

#---- sub code
#골드 바흐의 추측 계산을 위해 우선
#10000의 합을 나타내기 위해 10000까지 소수합을 구해둔다.
n = 10000
a = [False,False] + [True]*(n-1) #현재값이 소수인지 아닌지 저장용.
prime = []

for i in range(2, n+1):
    if a[i] == True: #소수인 경우 (2부터 시작하므로)
        prime.append(i)
        #다음 2x2, 2x3 등을 전부 지워준다.
        j = 2
        while i * j <= n:
            a[i*j] = False
            j += 1

#탐색에 활용하기 위한 소수 목록표를 set자료형으로 하나 더 만들어 준다.
table = set(prime)

#----main code

repeat_time = int(input().rstrip())

for _ in range(repeat_time):
    partition = []
    target = int(input().rstrip())
    idx = 0

    while True:
        #인덱스를 넘어가거나 target 값보다 커진경우.
        if idx > len(prime) - 1:
            break
        if prime[idx] > target:
            break

        if target - prime[idx] in table: #뽑아 놓은 소수 목록에 존재하면
            if (target - prime[idx], prime[idx]) in partition: #5,7 추가했는데 7,5를 또 추가하려고 하면 추가하지 않는다.
                pass
            else:
                partition.append((prime[idx], target - prime[idx])) # 골드바흐 파티션 하나를 완성하였다!
        idx += 1

    #10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다. (리스트는 비어있을 수 없다.)
    gap = abs(partition[0][0] - partition[0][1])
    result1 = partition[0][0]
    result2 = partition[0][1]

    for n1, n2 in partition:
        if abs(n1 - n2) < gap:
            result1 = n1
            result2 = n2
    print(result1, result2)