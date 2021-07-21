lst = []
string = input()
for char in string:
    lst.append(int(char))
lst.sort(reverse = True)

for char in lst:
    print(char, end = "")