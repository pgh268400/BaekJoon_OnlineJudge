n1 = int(input())
n2 = int(input())
n3 = int(input())

if(n1 + n2 + n3 == 180):
    if(n1 == 60 and n2 == 60 and n3 == 60):
        print("Equilateral")
    elif(n1 == n2 or n2 == n3 or n1 == n3):
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")