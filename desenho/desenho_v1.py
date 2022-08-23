import numpy as  np
import cv2 as cv
from skimage.segmentation import watershed
import skimage.morphology as mm

desenho = False
linha = False
circ = False
livre = False

ix = -1
iy = -1

troca_cor = 1

linha_colorida = [(0,255,255),(255,255,0),(0,255,0),(0,0,255),(205,90,106),
                  (0,255,127),(30,105,210),(130,0,75),(255,0,255),(255,0,0)]

linha_cinza = [(128,128,128),(79,79,79),(192,192,192),(169,169,169),(220,220,220),
               (255,255,255),(119,136,153),(47,79,79),(211,211,211),(105,105,105)]

point = list()

img = cv.imread('controle (45).jpg')


def desenho_livre(evento,x,y,flags,param):

    global ix, iy, desenho, livre, linha, circ, clear 
    
    if evento == cv.EVENT_LBUTTONDOWN:
        desenho = True
        ix = x 
        iy = y

    elif evento == cv.EVENT_MOUSEMOVE:
        if desenho == True and livre == True:
            cv.line(img, (ix,iy), (x,y), linha_colorida[troca_cor], 2)
            ix, iy = x, y
        
    elif evento == cv.EVENT_LBUTTONUP and livre == True:
        desenho = False
        cv.line(img, (ix,iy), (x,y), linha_colorida[troca_cor], 2)

    if evento == cv.EVENT_LBUTTONDOWN and circ == True:
        cv.circle(img,(x,y),20,(0,255,0),thickness=2)
        cv.circle(img,(x,y),1,(0,0,255),thickness=1)
        
    if evento == cv.EVENT_LBUTTONDOWN and linha == True:
        point.append((x,y))
        cv.circle(img,(x,y),2,(0,0,255),thickness=1)
        if len(point) % 2 == 0:
            cv.line(img, point[0], point[1],(0,255,0), 2)
            cv.circle(img,point[1],2,(0,0,255),thickness=1)
            point.clear()
    

cv.namedWindow(winname='meu_desenho')

cv.setMouseCallback('meu_desenho', desenho_livre)

while True:
    
    cv.imshow('meu_desenho', img)

    k = cv.waitKey(1)
       
    if k == ord('x') or k == ord('X'):
        break

    elif k == 27:
        circ = False
        linha = False
        livre = False
        desenho = False
        
    elif k > 0 and chr(k).isdigit():
        troca_cor = int(chr(k))

    elif k == ord('l') or k == ord('L'):
        linha = True
        circ = False
        livre = False

    elif k == ord('c') or k == ord('C'):
        circ = True
        linha = False
        livre = False

    elif k == ord('w') or k == ord('W'):
        circ = False
        linha = False
        livre = True
            
cv.destroyAllWindows()


# 8 conexo connectivity = 2
# 4 conexo connectivity = 1
