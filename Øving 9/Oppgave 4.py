__author__ = 'Morten Stulen'
def number_of_lines(filename):
    file = open(filename, "r")
    valueList = file.readlines()
    file.close()
    return len(valueList)
print(number_of_lines("nummer.txt"))

def number_frequency(filename):
    file = open(filename, "r")
    valueList = file.readlines()
    file.close()

    valueList = [word.strip() for word in valueList]

    valueSet = set(valueList)
    countDict = {}

    for i in valueSet:
        countDict[i] = valueList.count(i)

    return countDict


print(number_frequency("nummer.txt"))

countDict = number_frequency("nummer.txt")
for key, value in countDict.items():
    print(str(key) + ": " + str(value))

# for i in countDict:
#     print(str(i) + ": " + str(countDict[i]))

