from sys import stdin
x,y,w,h = map(int , stdin.readline().split())
lst2 = [x, y, w-x, h-y]
print(min(lst2))