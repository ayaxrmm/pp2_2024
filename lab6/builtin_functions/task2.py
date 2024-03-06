word = "ThisIsAExamPLe"
def count(word):
    uppersum = sum(chr.isupper() for chr in word)
    lowersum = sum(chr.islower() for chr in word)
    print("num of upper: ", uppersum)
    print("num of lower: ", lowersum)
count(word)
