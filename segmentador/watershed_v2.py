import numpy as  np
import cv2 as cv
from skimage.segmentation import watershed
import skimage.morphology as mm

desenho = False

ix = -1
iy = -1

troca_cor = 1
linha_colorida = [(0,255,255),(255,255,0),(0,255,0),(0,0,255),(205,90,106),
                  (0,255,127),(30,105,210),(130,0,75),(255,0,255),(255,0,0)]

linha_cinza = [(128,128,128),(79,79,79),(192,192,192),(169,169,169),(220,220,220),
               (255,255,255),(119,119,119),(47,47,47),(211,211,211),(105,105,105)]

img = cv.imread('controle (1).jpg')

img_c = cv.imread('controle (1).jpg',0)

# Parametros do filtro
B = np.array([[0,1,0],[1,1,1],[0,1,0]]) # 4-conexo
#B = np.ones((3,3))                     # 8-conexo

grad = mm.dilation(img_c,B) - mm.erosion(img_c,B)

img_copia = img.copy()

fundo_preto = np.zeros(img.shape[:2],dtype=np.int32)

def desenho_livre(evento,x,y,flags,param):

    global ix, iy, desenho
    
    if evento == cv.EVENT_LBUTTONDOWN:
        desenho = True
        ix = x
        iy = y

    elif evento == cv.EVENT_MOUSEMOVE:
        if desenho == True:
            cv.line(img_copia, (ix,iy), (x,y), linha_colorida[troca_cor], 3)
            cv.line(fundo_preto, (ix,iy), (x,y), linha_cinza[troca_cor], 3)
            ix, iy = x, y

    elif evento == cv.EVENT_LBUTTONUP:
        desenho = False
        cv.line(img_copia, (ix,iy), (x,y), linha_colorida[troca_cor], 3)
        cv.line(fundo_preto, (ix,iy), (x,y), linha_cinza[troca_cor], 3)

    elif evento == cv.EVENT_RBUTTONDOWN:
        cv.circle(img_copia,(x,y),20,linha_colorida[troca_cor],thickness=-1)
        cv.circle(fundo_preto,(x,y),20,linha_cinza[troca_cor],thickness=-1)

cv.namedWindow(winname='meu_desenho')

cv.setMouseCallback('meu_desenho', desenho_livre)

while True:
    
    cv.imshow('meu_desenho', img_copia)

    k = cv.waitKey(1)
       
    if k == 27: # tecla Esc
        break

    elif k == ord('s'):
        cv.imwrite('Marcador.jpg', fundo_preto)

    elif k == ord('w'):
        
        w = watershed(grad,markers=fundo_preto,connectivity=1)

        #w2 = mm.dilation(w) - mm.erosion(w)

        for linha in range(img.shape[0]):
            for coluna in range(img.shape[1]):
                if w[linha,coluna] == 79:
                    img[linha,coluna,2] = 0
                    img[linha,coluna,1] = 255
                    img[linha,coluna,0] = 255

        cv.imwrite('watershed.jpg', img)
        
    elif k > 0 and chr(k).isdigit():
        troca_cor = int(chr(k))
        
            
cv.destroyAllWindows()

# 8 conexo connectivity = 2
# 4 conexo connectivity = 1 

