from itertools import izip

with open("tag") as s, open("tfidf.txt") as t: 
    for x, y in izip(s, t):
        x = x.strip()
        y = y.strip()
        print("{0} {1}".format(x, y))
