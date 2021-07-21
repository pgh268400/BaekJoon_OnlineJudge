import collections


x_lst, y_lst = [], []
for _ in range(3):
    x,y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)


x_counter = collections.Counter(x_lst)
y_counter = collections.Counter(y_lst)

mx = max(x_counter, key=x_counter.get)
my = max(y_counter, key=y_counter.get)

del x_counter[mx]
del y_counter[my]

for x, counter in x_counter.items():
    print(x, end = " ")

for y, counter in y_counter.items():
    print(y, end = " ")