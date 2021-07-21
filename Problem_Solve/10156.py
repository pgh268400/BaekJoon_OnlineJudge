a,b,c = map(int , input().split())
need = a * b - c
if(need < 0): #음수면 돈을 이미 충분히 가지고있음.
    need = 0
print(need)