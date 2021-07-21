total_time = 0
word = input()
dial = ["ABC","DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
for w in word: #문자열 길이만큼 반복
        for d in dial:
            if w in d:
                total_time += dial.index(d) + 3
print(total_time)