count = 0
words = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatia:
    if c in words: #크로아티아 알파뱃 발견시
        count += words.count(c)
        words = words.replace(c, "*") #의미없는 문자로 치환
        

print(len(words.replace("*", "")) + count)  #의미없는 문자는 치우고 크로아티아 알파벳과 함께 카운팅