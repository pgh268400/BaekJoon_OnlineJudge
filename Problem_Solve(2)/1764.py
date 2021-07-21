from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())

no_listen = set([])
no_see = set([])

for i in range(N):
    no_listen.add(stdin.readline().rstrip())
for i in range(M):
    no_see.add(stdin.readline().rstrip())
no_listen_see = list(no_listen.intersection(no_see))
no_listen_see.sort()
print(len(no_listen_see))
for element in no_listen_see:
    print(element)