a,b,c,d,f = map(int , input().split())
chk_num = (a ** 2 + b ** 2 + c ** 2 + d ** 2 + f ** 2) % 10
print(chk_num)