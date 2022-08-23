import numpy as  np
import cv2 as cv

desenho = False

ix = -1
iy = -1

# EStilo em BGR
cor_linha = [(211,0,148),(255,0,255),(0,100,0)]

def desenho_livre(evento,x,y,flags,param):

    global ix, iy, desenho

    if evento == cv.EVENT_LBUTTONDOWN:
        desenho = True
        ix = x
        iy = y

    elif evento == cv.EVENT_MOUSEMOVE:
        if desenho == True:
            cv.line(img, (ix,iy), (x,y), cor_linha[1], 5)
            ix, iy = x, y
            print("COLUNA (eixo X):", x, "LINHA (eixo Y):", y)
            print("------ CANAIS -----")
            print("VERMELHO:", img[x,y,0], "VERDE:", img[x,y,1], "AZUL:", img[x,y,2])
            print("----------")
                
    elif evento == cv.EVENT_LBUTTONUP:
        desenho = False
        cv.line(img, (ix,iy), (x,y), cor_linha[1], 5)
        
cv.namedWindow(winname='meu_desenho')

cv.setMouseCallback('meu_desenho', desenho_livre)

img = cv.imread('controle (1).jpg')

while True:
    
    cv.imshow('meu_desenho', img)

    if cv.waitKey(20) & 0xFF == 27: # tecla Esc
        break

cv.destroyAllWindows()


