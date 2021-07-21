lst = [[1,1]]
idx = 2
count = 0

n = 1000000000
while True:
    end = lst[count][-1] + 1
    end2 = end + (count+1)*6 - 1
    if end2 > n:
        break
    lst.append([end, end2])
    count+= 1

a = int(input())
find = 0
for l in lst:
    if l[0] <= a and l[1] >= a:
        break
    find+=1
print(find+1)