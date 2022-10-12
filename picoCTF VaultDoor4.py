
#picoCTF VaultDoor4 Yassine SABIR <id = YsaB>


def Hex2int(ch):
    listalphanum=list("0123456789ABCDEF")
    return listalphanum.index(ch[1].upper())+16*listalphanum.index(ch[0].upper())


def bin2int(ch):
    if ch=="":
        return 0
    else:
        return int(ch[-1])+2*bin2int(ch[:-1])


def oct2int(ch):
    if ch=="":
        return 0
    else:
        return int(ch[-1])+8*oct2int(ch[:-1])



List=[106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
    "55", "6e", "43", "68", "5f", "30", "66", "5f",
    "0142", "0131", "0164", "063" , "0163", "0137", "0146", "064" ,
    'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ]

flag=""

for i in range(8):
    flag += chr(List[i])

for i in range(8,16):
    flag += chr(Hex2int(List[i]))

for i in range(16,24):
    flag += chr(oct2int(List[i]))

for i in range(24,32):
    flag += List[i]

print(flag)

