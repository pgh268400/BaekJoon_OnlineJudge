import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [False] * 1000001

    order_num = int(input())

    for key in range(order_num):
        order = input().rsplit()
        cmd, data = order[0], order[1]
        if cmd == 'I':
            #Interation 돌때 사용되는 i값(key값)을 id로 사용
            #딕셔너리로 사용시 연속된 값에 대해 대응하지 못했음. (물론 딕셔너리에 따른 별도 리스트로 구현가능함.)
            heapq.heappush(min_heap, (int(data), key))
            heapq.heappush(max_heap, (int(data) * -1, key))
            visit[key] = True #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif cmd == 'D':
            if data == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
                # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                while (min_heap and not visit[min_heap[0][1]]): # visit이 False일떄 -> 해당노드가 삭제된상태
                    heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if min_heap: #비었지 않으면
                    visit[min_heap[0][1]] = False # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
                    heapq.heappop(min_heap)
            elif data == '1':
                while (max_heap and not visit[max_heap[0][1]]): #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

# 모든 연산이 끝난후에도 쓰레기 노드가 들어있을수 있으므로, 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값을 출력한다. 
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        mx = heapq.heappop(max_heap)
        mi = heapq.heappop(min_heap)
        print(-mx[0], mi[0])
    else:
        print('EMPTY')