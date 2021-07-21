def check_group(words):
    idx = 0
    scan = ""
    lst = []
    for w in words:
        #print(w)
        if (idx == 0): #첫번째 항일경우
            scan = w #현재 글자를 저장한다
        if (scan != w): #다른 글자가 나오면
            lst.append(scan) #이전 글자를 리스트에 저장한다 (앞으로 이 글자는 나중에 나와선 안된다.)
            scan = w #스캔을 현재 글자부터 저장한다.
        if w in lst: #이 글자가 또 나와버린경우
            return False #그룹단어가 아니다.
        idx+=1
    return True #위검사에서 걸리지 않았으면 그룹단어이다.

group_word = 0
n = int(input())
for i in range(n): #들어온 숫자만큼 반복해 받는다.
    words = input()
    if (check_group(words) == True):
        group_word+=1
print(group_word)