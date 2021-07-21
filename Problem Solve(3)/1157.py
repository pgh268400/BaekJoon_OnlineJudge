#a~z => 97~122
#A~Z => 65~90

a = input().lower() #대소문자 구분안하니 전부 소문자로 바꿔줌.
lst = list(set(a)) #집합 자료형 변환 후 list로 변환
mx = []

for c in lst:
    mx.append(a.count(c))
if mx.count(max(mx)) == 1:
    mx_idx = mx.index(max(mx))
    print(lst[mx_idx].upper())
else:
    print("?")