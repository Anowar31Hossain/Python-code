file = open("Information.txt","r+")

# print(file.readable())
# text = file.read()
# print(text)
# size = len(text)
# print(size)

# text = file.readline()[14]
# print(text)

for line in file:
    print(line)

file.close()