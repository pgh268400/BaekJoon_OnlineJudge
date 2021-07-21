dice = list(map(int , input().split()))
dice_count = [dice.count(x) for x in range(1,7)]
#print(dice_count)
duplicate = max(dice_count)
noon = dice_count.index(duplicate) + 1
if(duplicate == 1): #전부 다르면
    print(max(dice) * 100) 
elif(duplicate == 2): #두개 같으면
    print(1000 + noon * 100)
elif(duplicate == 3): #전부 같으면
    print(10000 + noon * 1000)