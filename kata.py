# arr = ['testttt', 'test', 'testtt', 'testt']
# sorted = []
#
# def sortLength():
#     for word in arr:
#         length = len(word)
#         print(length)
#         sorted.append(word)
#     if length > len(sorted[0]):
#         sorted.insert(0, word)
#         return sorted
#
#     # if length
# sortLength()

conjoined = []
conjoinOperator = '+'

def digitDivide(word):
    word = str(word)
    for digit in word:
        conjoined.append(digit)
    conjoinOperator.join(conjoined)

    print(conjoined)

digitDivide(1394)
