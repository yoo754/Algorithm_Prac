# 1759 암호만들기

from itertools import combinations

L, C = map(int, input().split()) # L 비번수, C 가능성있는 단어

# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
# 증가하는 순서로 배열
# 소문자 아스키 a97 z122 ord() -> chr() 이용하면됨

password = list(map(ord, input().split()))
password = sorted(password)
vowel = list(map(ord, ['a','e','i','o','u']))
consonant = [i for i in range(97,123)]

for i in range(len(vowel)):
    consonant.remove(vowel[i])

for word in combinations(password, L):
    cnt_v = 0
    cnt_c = 0
    for i in range(len(vowel)):
        cnt_v += word.count(vowel[i])
    for j in range(len(consonant)):
        cnt_c += word.count(consonant[j])
    if cnt_v >= 1 and cnt_c >= 2 :
        word = sorted(word)
        for k in word:
            print(chr(k), end="")
        print()
