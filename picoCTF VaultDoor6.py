#picoCTF VaultDoor6 SABIR Yassine



def hex2int(h):
    if h=="":
        return 0
    else:
        L=list("0123456789ABCDEF")
        return 16*hextoint(h[:-1])+L.index(h[-1].upper())

def int2bin(n):
    if n==0:
        return "0"
    else:
        return int2bin(n//2)+str(n%2)

def list_len_8(ch):
    L="00000000"+ch
    return L[-8:]


def XOR(a,b):
    if a not in ["0","1"] or b not in ["0","1"]:
        return
    if a=="0":
        return b
    else:
        if b=="1":
            return "0"
        return "1"

def XOR_hex(h1,h2):

    bin1=list_len_8(int2bin(hex2int(h1)))
    bin2=list_len_8(int2bin(hex2int(h2)))

    result=""

    for i in range(8):
        result += XOR(bin1[i],bin2[i])

    return result

def bin2int(b):
    if b=="":
        return 0
    else:
        return 2*bin2int(b[:-1])+int(b[-1])

def main():

    LIST=['3b', '65', '21', 'a', '38', '0', '36', '1d', 'a', '3d', '61', '27', '11', '66', '27', 'a', '21', '1d', '61', '3b', 'a', '2d', '65', '27', 'a', '66', '36', '30', '67', '6c', '64', '6c']

    KEY="55"

    flag=""

    for l in LIST:
        flag+=chr(bin2int(XOR_hex(l,KEY)))

    print(flag)#n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919

main()