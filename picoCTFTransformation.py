#picoCTF Transformation Yassine SABIR

"""
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
"""

flag_encrypted = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"


def decode(flag_enc):
    flag=""
    for i in range(0,len(flag_enc)):
        flag += chr((ord(flag_enc[i]) >> 8))
        flag += chr(ord(flag_enc[i])%(2**8))
    return flag


print(decode(flag_encrypted))  #picoCTF{16_bits_inst34d_of_8_75d4898b}
