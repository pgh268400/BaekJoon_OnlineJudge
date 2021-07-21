word_list = []
n = int(input())
for i in range(n):
    word = input()
    element = (len(word), word)
    if not element in word_list: #중복검사
        word_list.append(element)
        
#sort함수 ::
#글자수, 글자의 형태로 넘기면
#앞의 글자수를 먼저 정렬하고 같으면 글자를 기준으로 정렬한다.
word_list.sort()
for length,word in word_list:
    print(word)