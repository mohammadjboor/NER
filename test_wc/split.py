with open("tag", "w") as tagfile, open("ANERCorp", "r") as src:
    lines = src.readlines()
    sent = ""
    tag = ""
    for l in lines:
        tokens = l.strip().split(" ")
        #word = tokens[0]
        t = tokens[1]
        print(t)
        #sent += word + " "
        #tag += t + " "
        ##print(tokens)
        #import pdb; pdb.set_trace()
        #if word == ".":
         #   srcfile.write(sent.strip() +'\n')
          #  sent = ""
           # tagfile.write(tag.strip() +'\n')
            #tag = ""
            
