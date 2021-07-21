idx = 1
self_lst = []

for i in range(1,10001):
    for char in str(i): #1~10001까지 각각 non_self_num을 만든다.
        i += int(char)
    if i <= 10000: 
        self_lst.append(i)
for i in range(1, 10001):
    if not i in self_lst:
        print(i)
    