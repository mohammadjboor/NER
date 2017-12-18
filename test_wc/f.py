with open("firsttoken", "w") as ft, open("ANERCorp", "r") as src:
    lines = src.readlines()
    for l in lines:
        tokens = l.strip().split(" ")
        word = tokens[0]
        #print(word)
        #import pdb; pdb.set_trace()
        ft.write(word +'\n')
