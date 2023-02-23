# picoCTF transposition-trial Yassine SABIR

corrupted_flag = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"

flag = ""

for i in range(0,len(corrupted_flag),3):
    if (i+2<len(corrupted_flag)):
        flag += corrupted_flag[i+2]
    flag += corrupted_flag[i]
    if (i+1<len(corrupted_flag)):
        flag += corrupted_flag[i+1]
    
print(flag)  #The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
