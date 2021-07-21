
n = int(input())
for i in range(n):
    score_lst = []
    upper_avg_person = 0
    
    #공백으로 구분해 받고 map 으로 int 변환 -> list로 리스트 변환
    score_lst = list(map(int, input().split()))
    avg = sum(score_lst[1:]) / score_lst[0]
    for j in range(1, len(score_lst)):
        if score_lst[j] > avg: #평균 넘으면
            upper_avg_person += 1
    upper_avg_percentage = upper_avg_person / score_lst[0] * 100
    print("{:.3f}%".format(upper_avg_percentage))