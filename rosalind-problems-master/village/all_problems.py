#import this
from collections import Counter
#
# ===== Variables and Some Arithmetic =====
# a = 943
# b = 970
# print(f'{a}^2 + {b}^2 = {a**2 + b**2}')

#
# # ===== Strings and Lists =====
# wordOneStartPos = 50
# wordOneEndPos = 64
#
# wordTwoStartPos = 99
# wordTwoEndPos = 107
#
# txtStr = "5gGg7EzJ6NGv6pmORO9UBIay7S9ASvWZJPTPtz3ihrNyLeDoP9Madagascarophisx88ym2c8574G21ol6Wb9jhve7X5t63iQHgsubrubrumi1puG8T3yc6rsDAcHtzteCufOC2CYIFfYuufg9HblK5prK4ZCI26ME0PXMfW9tMLKra8I."
#
# # Note: end position is not inclusive, so we add 1 to capture it
# print(
#     f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]}')
#cuts string twice

# # ===== Conditions and Loops =====
# startPos = 4263
# endPos = 8782
# result = 0

#
#
# for x in range(startPos, endPos + 1):
#     if x % 2 != 0:
#         result += x

#result = sum([x for x in range(startPos, endPos + 1) if x % 2 != 0] )

#print(result)


# # ===== Working with Files =====
# outputFile = []
#
# with open('input.txt', 'r') as f:
#     outputFile = [line for pos, line in enumerate(
#         f.readlines()) if pos % 2 != 0]
#     print(outputFile)
# #filters every other line
#
# with open('out.txt', 'w') as f:
#     f.write(''.join([line for line in outputFile]))


# # ===== Dictionaries =====
txtStr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

wordCoutDict = {}

for word in txtStr.split(' '):
    if word in wordCoutDict:
        wordCoutDict[word] += 1
    else:
        wordCoutDict[word] = 1
print (wordCoutDict)

# Optimized, Pythonic approach, using collections module:
# wordCoutDict = Counter(txtStr.split(' '))

for key, value in wordCoutDict.items():
     print(key, value)




#
# with open("input.txt", "r") as myfile:
#     data = myfile.readlines()
# wd ={}
# #words = data.split(" ")
# for i in data:
#     for d in i.split(" "):
#         #d = d.lower()
#         if '\n' in d:
#             d = d[:-2]
#         if d in wd:
#             wd[d] += 1
#         if d not in wd:
#             wd[d] = 1
#
# for i in wd:
#     print ('{} {}'.format(i,wd[i]))
#
#
