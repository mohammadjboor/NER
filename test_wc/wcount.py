import math
lines = open("firsttoken").readlines()
N = len(lines)
word_count = {}
for line in lines:
        word = line.strip()
        if word not in word_count:
                word_count[word]=0
        word_count[word]+=1
        tfidf = math.log(N/word_count[word])
        print(tfidf)
