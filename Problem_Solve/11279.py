from sys import stdin
input = stdin.readline
import heapq #힙 사용을 위해 import
#파이썬의 자료구조는 기본적으로 최소 힙임.
#heapq 모듈을 통해 원소를 추가하거나 삭제한 리스트가 최소 힙이다. 별도의 자료구조로 마련되어 있지 않음.


#최소 힙 자료구조에 따라 알아서 오름차순 정렬됨. 
heap = []

n = int(input().rstrip())
for i in range(n):
    x = int(input().rstrip())
    if(x == 0): #가장작은값 출력하는 연산.
        if not heap: #비었으면
            print(0)
        else:
            print(heapq.heappop(heap)[1]) #가장 작은값 뽑고 출력
    elif (x > 0): #x가 자연수라면 추가
        heapq.heappush(heap, (-x, x)) #최대힙 구현을 위해 꼼수 사용. (첫 요소 기준으로 판단하기 때문에 첫값을 마이너스로 넣어 준다.)
        #나중 인덱스 접근할땐 1번 인덱스로 접근하면댐.