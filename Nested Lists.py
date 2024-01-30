if __name__ == '__main__':
    details = []
    nameList = []
    scoreList = []
    N = int(input())
    if N>=2 and N <=5:
        for i in range(N):
            name = input()
            score = float(input())
            dtl = [name, score]
            details.append(dtl)
            nameList.append(name)
            scoreList.append(score)
        scoreList = list(set(scoreList))
        scoreList.sort()
        nameRes = []
        for j in details:
            if scoreList[1] == j[1]:
                nameRes.append(j[0])
        nameRes.sort()
        for k in nameRes:
            print(k)
            
