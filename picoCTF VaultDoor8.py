# picoCTF VaultDoor8 SABIR Yassine

def int2bin(integer):
    if integer==0:
        return "0"
    else:
        return int2bin(integer//2)+str(integer%2)
        
def bin2int(BIN):
    if BIN=="":
        return 0
    else:
        return 2*bin2int(BIN[:-1])+int(BIN[-1])
        
def hex2int(HEX):
    A = list("0123456789ABCDEF")
    if len(HEX) != 2:
        return
    else:
        return 16*A.index(HEX[0])+A.index(HEX[1])
        
def char2bin(char):
    BIN = int2bin(ord(char))
    BIN = "00000000"+BIN
    return BIN[-8:] 
    
    
def switchBits(char, p1, p2):
    BIN = char2bin(char)
    BIN_switch = ""
    for i in range(8):
        if i==p1:
            BIN_switch += BIN[p2]
        else:
            if i==p2:
                BIN_switch += BIN[p1]
            else:
                BIN_switch += BIN[i]
    return chr(bin2int(BIN_switch))
    
def descramble(cipherPassword):
    length = len(cipherPassword)
    password = ""
    for b in range(length):
        c = cipherPassword[length-1-b]
        c = switchBits(c,6,7)
        c = switchBits(c,2,5)
        c = switchBits(c,3,4)
        c = switchBits(c,0,1)
        c = switchBits(c,4,7)
        c = switchBits(c,5,6)
        c = switchBits(c,0,3)
        c = switchBits(c,1,2)
        password = c + password
    return password
    
def main():
    expected = ["F4", "C0", "97", "F0", "77", "97", "C0", "E4", "F0", "77", "A4", "D0", "C5", "77", "F4", "86", "D0", "A5", "45", "96", "27", "B5", "77", "D2", "D0", "B4", "E1", "C1", "E0", "D0", "D0", "E0"]
    
    cipherPassword = ""
    for HEX in expected:
        cipherPassword += chr(hex2int(HEX))
    
    print("flag is : ",descramble(cipherPassword)) #flag is :  s0m3_m0r3_b1t_sh1fTiNg_91c642112
    
main()

    
