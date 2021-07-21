n,m,k = map(int , input().split())
if k <= m-1: #번호가 m보다 작으면
    print(F"0 {k}") #그 숫자가 곧 좌표
else:
    n_location = k // m #값을 m으로 나눈것의 몫이 곧 n의 좌표.
    m_location = k % m
    print(n_location, m_location)