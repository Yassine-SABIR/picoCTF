
#picoCTF Yassine SABIR < id = YsaB >

import cv2
import numpy as np


scrambled1 = cv2.imread("C:/Users/hp/Downloads/scrambled1 (1).png")

scrambled2 = cv2.imread("C:/Users/hp/Downloads/scrambled2 (1).png")


n,m,k = scrambled1.shape

newimg=np.zeros((n,m,k),np.uint8)
oldimg = np.zeros((n,m,k),np.uint8)

for i in range(n):
    for j in range(m):

        newimg[i][j] = ((scrambled1[i][j][0]+scrambled2[i][j][0])%256,(scrambled1[i][j][1]+scrambled2[i][j][1])%256,(scrambled1[i][j][2]+scrambled2[i][j][2])%256)


cv2.imshow("neximg",newimg)
