#그리드 알고리즘 - 덧셈부분을 먼저 계산하는 것을 최적으로 한다.

val = 0
new = []
exp = input()

minus_split = exp.split("-")

for element in minus_split:
    plus_split = element.split("+")
    for pelement in plus_split:
        val += int(pelement)
    new.append(val)
    val = 0

for i in range(len(new)):
    if(i == 0):
        first = new[i]
    else:
        first = first - new[i]
print(first)