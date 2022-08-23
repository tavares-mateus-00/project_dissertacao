import numpy as  np
import cv2 as cv

desenho = False
ix = -1
iy = -1

cor_linha = [(255,255,0),(0,0,255),(200,50,100)]

def desenho_livre(evento,x,y,flags,param):

    global ix, iy, desenho

    if evento == cv.EVENT_LBUTTONDOWN:
        desenho = True
        ix = x
        iy = y

    elif evento == cv.EVENT_MOUSEMOVE:
        if desenho == True:
            #cv.circle(img, (x,y), 5, cor_linha[0], -1)
            cv.line(img, (ix,iy), (x,y), cor_linha[0], 2)

    elif evento == cv.EVENT_LBUTTONUP:
        desenho = False
        #cv.circle(img, (x,y), 5, cor_linha[0], -1)
        cv.line(img, (ix,iy), (x,y), cor_linha[0], 2)
        

cv.namedWindow(winname='meu_desenho')

cv.setMouseCallback('meu_desenho', desenho_livre)

img = cv.imread('controle (1).jpg')

while True:
    
    cv.imshow('meu_desenho', img)

    if cv.waitKey(20) & 0xFF == 27:
        cv.imwrite('salva.jpg',img)
        break

cv.destroyAllWindows()
