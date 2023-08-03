#picoCTF WhitePages SABIR Yassine

file = open("Downloads/whitepages.txt", "r")

content = file.read()

flag = ""

characters = []

for character in content:
    if ord(character) not in characters:
        characters.append(ord(character))

    if character == " ":
        flag += "1"
    else:
        flag += "0"

print(characters)# this shows that we only have 2 characters in the file, which are chr(8195) and chr(32)

print(flag)

flagtxt = ""

for i in range(0, len(flag),8):
    flagtxt += chr(int(flag[i:i+8],2))
print(flagtxt)
"""	picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_7100860b0fa779a5bd8ce29f24f586dc}"""
file.close()
