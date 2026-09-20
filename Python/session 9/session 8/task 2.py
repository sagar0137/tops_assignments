#Given a list of cricket scores [45, 78, 102, 34, 67, 89], use a while loop to print each score until you reach a score above 100,
#  then stop printing

scores = [45, 78, 102, 34, 67, 89]

i = 0

while i < len(scores):
    if scores[i] > 100:
        break
    print(scores[i])
    i += 1
