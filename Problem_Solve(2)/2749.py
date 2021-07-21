#주기의 길이가 P면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같습니다.

mod = 1000000
p = 1500000

n = int(input())

list = [0,1]
for i in range(2,p): #1500000까지 반복
    list.append(list[i-2] + list[i-1]) #피보나치 수열을 만든다.
    list[i] = list[i] % mod #mod로 나눠준다.
print(list[n % p]) 