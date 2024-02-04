import matplotlib.pyplot as plt
import numpy as np
import skimage.morphology as mm
from skimage import io
from skimage.measure import label, regionprops
#from skimage.color import label2rgb

def sobreposicao(image,binario):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if binario[i,j] == 1 or binario[i,j] == 255:
                image[i,j,0] = 255
                image[i,j,1] = 255
                image[i,j,2] = 0
    return image

def abe_rec(img,B):
    ero = mm.erosion(img,B)
    F = ero # semente
    G = img # mascara
    resultado = mm.reconstruction(F, G, method='dilation')
    return resultado

def fec_rec(img,B):
    dil = mm.dilation(img,B)
    F = dil # semente
    G = img # mascara
    resultado = mm.reconstruction(F, G, method='erosion')
    return resultado

name = ''
img = io.imread(name)

# INÍCIO ASF -> FECHAMENTO ABERTURA.

r = img[:,:,0]

asf_rec_fa = []

n = 13

e_e = mm.disk(1)

fec_r = fec_rec(r,e_e)
abe_r = abe_rec(fec_r,e_e)
asf_rec_fa.append(abe_r)

for i in range(2,n):
    fec_r = fec_rec(abe_r,mm.disk(i))
    abe_r = abe_rec(fec_r,mm.disk(i))
    asf_rec_fa.append(abe_r)

# FIM ASF -> FECHAMENTO ABERTURA.

i = #posição do vetor asf_rec_fa.
a = 255*mm.local_minima(asf_rec_fa[i])

imagem_rotulada = label(a)

p = []       # coordenadas
imagens = [] # imagens
limiar = 0.6

#imagem_rotulada_colorida = label2rgb(imagem_rotulada, image=a, bg_label=0)

for region in regionprops(imagem_rotulada):
    circularidade = (4 * np.pi * region.area)/(region.perimeter**2)
    if circularidade >= limiar:
        minr, minc, maxr, maxc = region.bbox
        imagens.append(a[minr:maxr,minc:maxc])
        p.append([minc,minr,abs(minc-maxc),abs(minr-maxr)])

mascara = np.zeros((img.shape[0],img.shape[1]), dtype=np.uint8)
for k in range(len(p)):
    for i in range(p[k][1],p[k][1]+p[k][3]-1):
        for j in range(p[k][0],p[k][0]+p[k][2]-1):
                if imagens[k][i-p[k][1],j-p[k][0]] != 0:
                        mascara[i,j] = 255

B = np.array([[0,1,0],[1,1,1],[0,1,0]])
contorno = mascara - mm.erosion(mascara,B1)

plt.imshow(sobreposicao(img, contorno));
plt.axis('off');
