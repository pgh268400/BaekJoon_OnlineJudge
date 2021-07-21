def check_hansu(n):
    if n < 100: #2자리수까진 전부 한수로 인정함. 
        return True
    else:
        lst = []
        chk = [] #체크용 리스트
        for char in str(n):
            lst.append(char)
        for i in range(1, len(lst)):
            distance = int(lst[i]) - int(lst[i-1])
            chk.append(distance)
        chk = set(chk) #set을 이용해 중복제거
        if (len(chk) == 1): #등차수열을 이룬경우
            return True
        else:
            return False

hansu_n = 0
n = int(input())
for i in range(1,n+1):
    if (check_hansu(i) == True):
        hansu_n += 1
print(hansu_n)