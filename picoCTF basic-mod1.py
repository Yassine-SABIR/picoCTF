# picoCTF basic-mod1 Yassine SABIR

LIST = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")

flagenc=[54,396,131,198,225,258,87,258,128,211,57,235,114,258,144,220,39,175,330,338,297,288]

flag=""
for l in flagenc:
   flag += LIST[l%37]

print(flag)#R0UND_N_R0UND_79C18FB3