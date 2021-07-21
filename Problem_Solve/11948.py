a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
lst1 =  [a,b,c,d]
lst2 = [e,f]
lst1.remove(min(lst1)) #제일 작은거 삭제
max_ef = max(lst2)
print(sum(lst1) + max_ef)