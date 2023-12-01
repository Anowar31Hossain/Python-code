import re
# pattern = r"Black"
# if re.match(pattern,"Black is a color,I love black color"):
#     print("Match")
# else:
#     print("Not match") 

# pattern = r"Black"
# if re.search(pattern,"Black is a color,I love Black color"):
#     print("Match")
# else:
#     print("Not match") 

# pattern=r"arafat"
# print(re.findall(pattern,"arafar is a talented boy,everytime arafat see the mobile."))

pattern=r"color"
text="My favourite color is black."
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())