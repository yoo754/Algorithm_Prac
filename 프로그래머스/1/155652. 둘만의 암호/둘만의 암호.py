def solution(s, skip, index):
    answer = []
    org = list(s)
    skip_list = list(skip)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    
    for word in skip_list:
        if word in alphabet:
            alphabet.remove(word)
                    
    for fin in org:
        idx = (alphabet.index(fin) + index) % len(alphabet)
        answer.append(alphabet[idx])
    
    return ''.join(answer)