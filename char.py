def findMax(words):
    maxim = max(words, key = len)
    max_words = ""
    for i in range(len(words)):
        if len(words[i]) == len(maxim):
            max_words += words[i] + "; "
    return max_words

def changeByRules(words):
    new = ""
    for a in words:
        if len(a) < 5 and a.isdigit():
            while len(a) < 5:
                a = "0" + a
            new += a + " "
            continue
        if a.isalpha():
            a = a[::-1]
            new += a + " "
            continue
        new += a + " "
    return new
    
    
str = input()
words = str.split()
try:
    if len(words) < 2:
        raise ValueError("need more words")

    print(findMax(words))
    
    print(changeByRules(words))
    
except ValueError as e:
    print(e)