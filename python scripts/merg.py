from itertools import izip

with open("src") as s, open("tag") as t: 
    for x, y in izip(s, t):
        x = x.strip()
        y = y.strip()
        print("{0}\t{1}".format(x, y))
