import numpy as  np
import cv2 as cv

def desenho_circulo(event,x,y,flags,param):

    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),50,(0,255,0),3)

    if event ==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),50,(0,255,255),3)
    

cv.namedWindow(winname='meu_desenho')

cv.setMouseCallback('meu_desenho', desenho_circulo)

img = cv.imread('controle (1).jpg')

while True:
    
    cv.imshow('meu_desenho', img)
    
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
