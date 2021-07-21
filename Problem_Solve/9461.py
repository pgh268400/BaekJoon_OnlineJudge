#점화식 d(i) = d(i - 1) + d(i - 5)
#d(i) 라는 큰 문제를 d (i - 1) 과 d (i - 5) 라는 작은문제로 쪼개서 구할 수 있다 ! => DP 문제

repeat = int(input())

for _ in range(repeat):
    n = int(input())
    pado = [None, 1, 1, 1, 2 , 2 , 3 ,4 , 5 , 7 ,9 , 12 , 16 ] + [0] * 100
    for i in range(13, n+1):
        pado[i] = pado[i - 1] + pado[i - 5]
    print(pado[n])