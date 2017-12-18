lines = open("ANERCorp").readlines()

words = []
labels = []
for line in lines:
    tokens = line.split()
    words.append(tokens[0])
    labels.append(tokens[1])
    
# Convert words to tf-idf

