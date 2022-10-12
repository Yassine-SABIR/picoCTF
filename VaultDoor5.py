


# picoCTF VaultDoor5 SABIR Yassine

def int2bin(n):
    if n==0:
        return "0"
    else:
        return int2bin(n//2) + str(n%2)

def hex2bin(ch):
    if len(ch) != 2:
        return
    listalphanum=list("0123456789abcdef")
    return ("0000" + int2bin(int(listalphanum.index(ch[0].lower()))))[-4:] + ("0000" + int2bin(int(listalphanum.index(ch[1].lower()))))[-4:]

def XOR(a,b):
    if a=="0" and b=="0":
        return "0"
    elif a=="1" and b=="1":
        return "0"
    else:
        return "1"

def HexXOR(h1,h2):
    b1=hex2bin(h1)
    b2=hex2bin(h2)
    b3=""
    for i in range(8):
        b3 += XOR(b1[i],b2[i])
    return b3

def bin2int(ch):
    if ch == "":
        return 0
    else:
        return int(ch[-1]) + 2 * bin2int(ch[:-1])

List=["3b", "65", "21", "0a" , "38", "00" , "36", "1d",
    "0a" , "3d", "61", "27", "11", "66", "27", "0a" ,
    "21", "1d", "61", "3b", "0a" , "2d", "65", "27",
    "0a" , "66", "36", "30", "67", "6c", "64", "6c"]

flag = ""
key = "55"
for i in List:
    flag += chr(bin2int(HexXOR(i,key)))
print(flag)