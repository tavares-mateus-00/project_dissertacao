import skimage.morphology as mm
from skimage import io

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
