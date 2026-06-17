def solution(message, spoiler_ranges):
    answer = 0
    
    idx = 0
    words = []
    for word in message.split() :
        word_start = message.find(word, idx)
        word_end = word_start + len(word) -1
        words.append((word, word_start, word_end))
        idx = word_end + 1
    
    # print(words)
    
    # 조건 1 스포 구간임?
    def is_spo(ws,we):
        for s, e in spoiler_ranges:
            if ws <= e and we >= s:
                return True
        return False
    
    # 조건 2 스포방지 구간 아님
    non_spo_words = set()
    for word, ws, we in words:
        if not is_spo(ws, we):
            non_spo_words.add(word)
    
    # 조건 3 스포구간 단어임        
    fin = []
    for word, ws, we in words:
        if is_spo(ws, we):
            fin.append(word)
    
    # 조건 4 스포방지구간 아닌곳에도 없고, 이전 스포구간에도 없음
    seen = set()
    for word in fin:
        if word  not in non_spo_words and word not in seen:
            answer +=1
        seen.add(word)

    return answer