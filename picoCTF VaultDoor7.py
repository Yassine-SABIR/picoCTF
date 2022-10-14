#picoCTF VaultDoor 7 SABIR YASSINE

def int2bin(n):
    if n==0:
        return "0"
    return int2bin(n//2)+str(n%2)

def str_len_8(l):
    S="0"*8+l
    return S[-8:]

def str_len_32(l):
    S="0"*32+l
    return S[-32:]

def ASCII2bin(a):
    return str_len_8(int2bin(ord(a)))

def hex2int(h):
    if h=="":
        return 0
    else:
        L=list("0123456789ABCDEF")
        return 16*hex2int(h[:-1])+L.index(h[-1].upper())

def bin2int(b):
    if b=="":
        return 0
    return int(b[-1])+2*bin2int(b[:-1])

def bin2ASCII(b):
    return chr(bin2int(b))

def encrypt(S):
    result=""

    for l in S:
        result+=ASCII2bin(l)

    return result

def char32_to_list_int(S):
    if len(S)!=32:
        print("ERROR")
        return
    LIST=[]
    for i in range(0,32,4):
        LIST+=[bin2int(encrypt(S[i:i+4]))]

    return LIST

def decrypt(b):
    result=""

    for i in range(0,len(b),8):
        result+=bin2ASCII(b[i:i+8])

    return result


def main():
    LIST=[1096770097, 1952395366, 1600270708,1601398833,1716808014, 1734293296, 842413104, 1684157793]

    flag=""

    for i in LIST:
        flag+=decrypt(str_len_32(int2bin(i)))
    print(flag)#A_b1t_0f_b1t_sh1fTiNg_702640db5a

main()
