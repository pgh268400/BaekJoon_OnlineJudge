n = int(input())
strings = input()
value = 0
for i in range(n):
    code = ord(strings[i]) - 96
    value += code * (31 ** i)
print(value % 1234567891)