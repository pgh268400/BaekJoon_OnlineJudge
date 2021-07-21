import math
diagonal, height_proportion, width_proportion = map(int , input().split())
n = (diagonal ** 2 / (height_proportion ** 2 + width_proportion ** 2))
n = math.sqrt(n)
print(int(n * height_proportion), int(n * width_proportion)) #int는 소수점 '버림' 임.
