import cv2 as cv
import numpy as np
import skimage.morphology as mm
from skimage.filters import threshold_otsu, threshold_local

name = '' 

a = cv.imread(name)

r = a[:,:,2]

vr = threshold_otsu(r)
loc_r3 = (threshold_local(r, block_size=7, method='gaussian') >= vr)

#*#*#*#*# Operações morfológicas #*#*#*#*#

img = 1 - loc_r3    

if img[-1,:].sum() != 0 or img[0,:].sum() != 0 or img[:,0].sum() != 0 or img[:,-1].sum() != 0:
    img[-1,:] = 0
    img[0,:] = 0 
    img[:,0] = 0
    img[:,-1] = 0

B = mm.disk(8)

dil = mm.dilation(img,B)
op1 = mm.reconstruction(dil,img, method='erosion')

B2 = mm.disk(5)
abe = mm.opening(op1,B2)

B1 = np.array([[0,1,0],[1,1,1],[0,1,0]])
contorno = abe - mm.erosion(abe,B1)