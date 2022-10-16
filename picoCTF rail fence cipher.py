
#picoCTF rail fence cipher Yassine SABIR 


enc = list("Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6")

rails = 4

n = len(enc)  # 56

m = n//(2*(rails-1)) # 9

r = n%(2*(rails-1)) # 2

first_ligne_len = 1+m

second_ligne_len = 1+2*m

third_ligne_len = 2*m

forth_ligne_len = m

first_ligne = enc[:first_ligne_len]

second_ligne = enc[first_ligne_len : first_ligne_len + second_ligne_len]

third_ligne = enc[first_ligne_len + second_ligne_len : first_ligne_len + second_ligne_len + third_ligne_len]

forth_ligne = enc[first_ligne_len + second_ligne_len + third_ligne_len :]

flag = ""

while first_ligne!=[] or second_ligne!=[] or third_ligne!=[] or forth_ligne!=[]:

    if first_ligne != []:
        flag += first_ligne[0]
        first_ligne = first_ligne[1:]

    if second_ligne != []:
        flag += second_ligne[0]
        second_ligne = second_ligne[1:]

    if third_ligne != []:
        flag += third_ligne[0]
        third_ligne = third_ligne[1:]

    if forth_ligne != []:
        flag += forth_ligne[0]
        forth_ligne = forth_ligne[1:]

    if third_ligne != []:
        flag += third_ligne[0]
        third_ligne = third_ligne[1:]

    if second_ligne != []:
        flag += second_ligne[0]
        second_ligne = second_ligne[1:]

print(flag)  #WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997
