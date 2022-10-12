
#picoCTF VaultDoor3 Yassine SABIR 

enc_flag="jU5t_a_sna_3lpm12g94c_u_4_m7ra41"


def decode(ch):
    if len(ch)!=32:
        return

    newch=list("jU5t_a_sna_3lpm12g94c_u_4_m7ra41")

    for i in range(8,16):
        newch[i] = ch[23-i]

    for i in range(16,32,2):
        newch[i] = ch[46-i]

    return newch

print(decode(enc_flag))
