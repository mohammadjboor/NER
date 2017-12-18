with open("ANERCorp", "r") as src:
    lines = src.readlines()
    data = []
    label = []
    for l in lines:
        tokens = l.strip().split(" ")
        data += [tokens[0]]
        label += [tokens[1]]

train_data = data[: int(len(data) * 0.80) ]
train_labels = label[: int(len(label) * 0.80) ]

test_data = data[: int(len(data) * 0.20) ]
test_labels = label[: int(len(label) * 0.20) ]


print(train_data)
print(train_labels)

print(len(train_data))
print(len(train_labels))

