english = int(input())
englishRoll = list(map(int, input().split()))
french = int(input())
frenchRoll = list(map(int, input().split()))
res = []
for i in englishRoll:
    for j in frenchRoll:
        if i == j:
          res.append(j)
englishRem = [element for element in englishRoll if element not in res]
frenchRem = [element for element in frenchRoll if element not in res]
print(len(englishRem) + len(frenchRem))
