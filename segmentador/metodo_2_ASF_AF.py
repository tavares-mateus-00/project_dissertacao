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

asf_rec_af = []

n = 13

e_e = mm.disk(1)

abe_r = abe_rec(r,e_e)
fec_r = fec_rec(abe_r,e_e)
asf_rec_af.append(fec_r)

for i in range(2,n):
    abe_r = abe_rec(fec_r,mm.disk(i))
    fec_r = fec_rec(abe_r,mm.disk(i))
    asf_rec_af.append(fec_r)
