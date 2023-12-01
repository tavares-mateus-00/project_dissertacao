import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np
import skimage.morphology as mm
from skimage.filters import threshold_otsu, threshold_local
from skimage import io

# box_list é a lista com as coordenadas dos objetos encontrado pela YOLO.
# image_name é a imagem que a YOLO processou. 

p = box_list

cont = io.imread(image_name)
k = -1
im = 0

mascara = np.zeros((cont.shape[0],cont.shape[1]), dtype=np.uint8)

geometria = 1

area, perimetro = [], []

for image in range(len(p)):

    k = k + 1
    r = cont[p[image][1]:p[image][3], p[image][0]:p[image][2], 0]

    vr = threshold_otsu(r)
    loc_r3 = (threshold_local(r, block_size=7, method='gaussian') >= vr)

    img = 1 - loc_r3


    if img[-1,:].sum() != 0 or img[0,:].sum() != 0 or img[:,0].sum() != 0 or img[:,-1].sum() != 0:
        img[-1,:], img[0,:], img[:,0], img[:,-1] = 0, 0, 0, 0

    B = mm.disk(8)
    dil = mm.dilation(img,B)
    op1 = mm.reconstruction(dil,img, method='erosion')

    B2 = mm.disk(5)
    abe = (mm.opening(op1,B2))*255
    area.append(abe.sum())

    B1 = np.array([[0,1,0],[1,1,1],[0,1,0]])
    contorno = abe - mm.erosion(abe,B1)
    perimetro.append(contorno.sum())

    im += 1

    for i in range(p[k][1],p[k][3]-1):
        for j in range(p[k][0],p[k][2]-1):
            if abe[i-p[k][1],j-p[k][0]] == 255:
                mascara[i,j] = 255
            if contorno[i-p[k][1],j-p[k][0]] == 255 and geometria == 1:
                cont[i,j,0] = 0
                cont[i,j,1] = 255
                cont[i,j,2] = 255
            if abe[i-p[k][1],j-p[k][0]] == 255 and geometria == 2:
                cont[i,j,0] = 0
                cont[i,j,1] = 255
                cont[i,j,2] = 255

font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
color = (255,255,255)
thickness = 2

for i in range(len(p)):
    x = p[i][0]
    y = p[i][1]
    cv.putText(cont, str(i), (x,y), font, fontScale, color, thickness, cv.LINE_AA)

plt.figure(figsize=(10,10))
plt.axis('off');
plt.imshow(cont);