import numpy as  np
import cv2 as cv
import math as mt

desenho = False
borracha = False
livre = False
desenho1 = False
circ = False
cortar = False 

jx = -1
jy = -1

ix = -1
iy = -1

kx = -1
ky = -1

wx = -1
wy = -1

troca_cor = 1
linha_colorida = [(0,255,255),(255,255,0),(0,255,0),(0,0,255),(205,90,106)]

img = cv.imread()

img_copia = img.copy()

def clear(x,y,jx,jy):
    for coluna in range(x,jx+1,1):
        for linha in range(y,jy+1,1):
            if img_copia[linha,coluna,0] == linha_colorida[troca_cor][0] and img_copia[linha,coluna,1] == linha_colorida[troca_cor][1] and img_copia[linha,coluna,2] == linha_colorida[troca_cor][2]:
                img_copia[linha,coluna,0] = img[linha,coluna,0]
                img_copia[linha,coluna,1] = img[linha,coluna,1]
                img_copia[linha,coluna,2] = img[linha,coluna,2]

def raio(x,y,kx,ky):
    return int(mt.sqrt((x - kx)**2 + (y - ky)**2))

def desenho_livre(evento,x,y,flags,param):

    global ix, iy, jx, jy, kx, ky, wx, wy, borracha, desenho1, desenho, livre, circ, cortar

    if evento == cv.EVENT_LBUTTONDOWN and livre == True:
        desenho = True
        ix = x
        iy = y

    elif evento == cv.EVENT_MOUSEMOVE:
        if desenho == True:
            cv.line(img_copia, (ix,iy), (x,y), linha_colorida[troca_cor], 2)
            ix, iy = x, y

    elif evento == cv.EVENT_LBUTTONUP and livre == True:
        desenho = False
        cv.line(img_copia, (ix,iy), (x,y), linha_colorida[troca_cor], 2)

    if evento == cv.EVENT_LBUTTONDOWN and borracha == True:
        jx,jy = x,y

    elif evento == cv.EVENT_LBUTTONUP and borracha == True:
        #cv.rectangle(img_copia,(jx,jy),(x,y),(0,255,0),1)
        clear(jx,jy,x,y)
        clear(x,y,jx,jy)

    if evento == cv.EVENT_LBUTTONDOWN and circ == True:
        kx, ky = x, y

    elif evento == cv.EVENT_LBUTTONUP and circ == True:
        cv.circle(img_copia,(kx,ky),raio(x,y,kx,ky),(0,255,0),thickness=2)
        cv.circle(img_copia,(kx,ky),1,(0,0,255),thickness=1)

    if evento == cv.EVENT_LBUTTONDOWN and cortar == True:
        wx, wy = x, y

    elif evento == cv.EVENT_LBUTTONUP and cortar == True:
        cv.rectangle(img_copia,(wx,wy),(x,y),(0,255,0),1)
        img_cortada = img_copia[wy+1:y,wx+1:x]
        cv.imshow("IMAGEM CORTADA", img_cortada)
        #cv.imwrite('cortada1.jpg', img_cortada)

cv.namedWindow(winname='meu_desenho')

cv.setMouseCallback('meu_desenho', desenho_livre)

while True:
    
    cv.imshow('meu_desenho', img_copia)

    k = cv.waitKey(1)
       
    if k == 27: # tecla Esc
        break
        
    elif k > 0 and chr(k).isdigit():
        troca_cor = int(chr(k))

    elif k == ord('b'):
        print('b')
        borracha = True
        livre = False

    elif k == ord('l'):
        print('l')
        borracha = False
        livre = True

    elif k == ord('c') or k == ord('C'):
        print('CIRCUNFERêNCIA')
        circ = True
        livre = False
        borracha = False

    elif k == ord('p') or k == ord('P'): # Função TESOURA. Recorta a região escolhida pelo usuário.
        print('TESOURA')
        circ = False
        livre = False
        borracha = False
        cortar = True

        #cv.imshow("IMAGEM CORTADA", img_cortada)
        
cv.destroyAllWindows()
