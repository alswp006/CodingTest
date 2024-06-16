from itertools import combinations
def solution(relation):
    columns = len(relation[0])
    rows = len(relation)

    answers = []

    for i in range(1,columns+1):
        # 후보키 경우의 수
        candidates = list(combinations(range(columns),i))

        for candidate in candidates:
            tples = []
            for row in relation:
                tple =[]
                for idx in candidate:
                    tple.append(row[idx])

                if tple not in tples:
                    tples.append(tple)

            if len(tples) == rows:
                answers.append(set(candidate))

    answers_ = answers.copy()
    print(answers)
    for i in range(len(answers)):
        for j in range(i+1,len(answers)):
            key1 = answers[i]
            key2 = answers[j]
            if key1.issubset(key2):
                try:
                    answers_.remove(key2)
                except:
                    continue

    print(answers_)
    return len(answers_)