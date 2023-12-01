import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu, threshold_local

name = ''

a = cv.imread(name)

# linha 1 e 2

b = a[:,:,0]           # canal azul  
g = a[:,:,1]           # canal verde
r = a[:,:,2]           # canal vermelho

x = cv.equalizeHist(b) # equalização do canal azul
y = cv.equalizeHist(g) # equalização do canal verde
z = cv.equalizeHist(r) # equalização do canal vermelho

# th normal \---\ 3 e 4

th = 127               # parâmetro careado

#thb = (b >= th)*255
thg = (g >= th)*255
thr = (r >= th)*255

#thx = (x >= th)*255
thy = (y >= th)*255
thz = (z >= th)*255

# th otsu \---\ 5 e 6

vb = threshold_otsu(b)
#print(vb)
vg = threshold_otsu(g)
#print(vg)
vr = threshold_otsu(r)
#print(vr)

veqb = threshold_otsu(x)
#print(veqb)
veqg = threshold_otsu(y)
#print(veqg)
veqr = threshold_otsu(z)
#print(veqr)

# Utilizando o limiar **** vb **** em todos os canais.

#th_ot_b0 = (b >= vb)*255
th_ot_r0 = (g >= vb)*255
th_ot_g0 = (r >= vb)*255

# Utilizando o limiar **** vg **** em todos os canais.

#th_ot_b1 = (b >= vg)*255
th_ot_r1 = (g >= vg)*255
th_ot_g1 = (r >= vg)*255

# Utilizando o limiar **** vr **** em todos os canais.

#th_ot_b2 = (b >= vr)*255
th_ot_r2 = (g >= vr)*255
th_ot_g2 = (r >= vr)*255

# Utilizando o limiar **** veqb **** em todos os canais.

#th_ot_b3 = (b >= veqb)*255
th_ot_r3 = (g >= veqb)*255
th_ot_g3 = (r >= veqb)*255

# Utilizando o limiar **** veqg **** em todos os canais.

#th_ot_b4 = (b >= veqg)*255
th_ot_r4 = (g >= veqg)*255
th_ot_g4 = (r >= veqg)*255

# Utilizando o limiar **** veqr **** em todos os canais.

#th_ot_b5 = (b >= veqr)*255
th_ot_r5 = (g >= veqr)*255
th_ot_g5 = (r >= veqr)*255

## Utilizando o limiar **** vb **** na equalização.

#th_ot_x0 = (x >= vb)*255
th_ot_y0 = (y >= vb)*255
th_ot_z0 = (z >= vb)*255

## Utilizando o limiar **** vg **** na equalização.

#th_ot_x1 = (x >= vg)*255
th_ot_y1 = (y >= vg)*255
th_ot_z1 = (z >= vg)*255

## Utilizando o limiar **** vr **** na equalização.

#th_ot_x2 = (x >= vr)*255
th_ot_y2 = (y >= vr)*255
th_ot_z2 = (z >= vr)*255

## Utilizando o limiar **** veqb **** na equalização.

#th_ot_x3 = (x >= veqb)*255
th_ot_y3 = (y >= veqb)*255
th_ot_z3 = (z >= veqb)*255

## Utilizando o limiar **** veqg **** na equalização.

#th_ot_x4 = (x >= veqg)*255
th_ot_y4 = (y >= veqg)*255
th_ot_z4 = (z >= veqg)*255

## Utilizando o limiar **** veqr **** na equalização.

#th_ot_x5 = (x >= veqr)*255
th_ot_y5 = (y >= veqr)*255
th_ot_z5 = (z >= veqr)*255

###########################################################################

# th local 

### Limiar th = 127

#leq_b0 = (threshold_local(b, block_size=7, method='gaussian') >= th)
loc_g0 = (threshold_local(g, block_size=7, method='gaussian') >= th)
loc_r0 = (threshold_local(r, block_size=7, method='gaussian') >= th)

### Limiar vb

#leq_b1 = (threshold_local(b, block_size=7, method='gaussian') >= vb)
loc_g1 = (threshold_local(g, block_size=7, method='gaussian') >= vb)
loc_r1 = (threshold_local(r, block_size=7, method='gaussian') >= vb)

### Limiar vg

#leq_b2 = (threshold_local(b, block_size=7, method='gaussian') >= vg)
loc_g2 = (threshold_local(g, block_size=7, method='gaussian') >= vg)
loc_r2 = (threshold_local(r, block_size=7, method='gaussian') >= vg)

### Limiar vr

#leq_b3 = (threshold_local(b, block_size=7, method='gaussian') >= vr)
loc_g3 = (threshold_local(g, block_size=7, method='gaussian') >= vr)
loc_r3 = (threshold_local(r, block_size=7, method='gaussian') >= vr)

### Limiar veqb

#leq_b4 = (threshold_local(b, block_size=7, method='gaussian') >= veqb)
loc_g4 = (threshold_local(g, block_size=7, method='gaussian') >= veqb)
loc_r4 = (threshold_local(r, block_size=7, method='gaussian') >= veqb)

### Limiar veqg

#leq_b5 = (threshold_local(b, block_size=7, method='gaussian') >= veqg)
loc_g5 = (threshold_local(g, block_size=7, method='gaussian') >= veqg)
loc_r5 = (threshold_local(r, block_size=7, method='gaussian') >= veqg)

### Limiar veqr

#leq_b6 = (threshold_local(b, block_size=7, method='gaussian') >= veqr)
loc_g6 = (threshold_local(g, block_size=7, method='gaussian') >= veqr)
loc_r6 = (threshold_local(r, block_size=7, method='gaussian') >= veqr)

#########################################################################

### Limiar th = 127

#leq_b0 = (threshold_local(b, block_size=7, method='gaussian') >= th)
loc_y0 = (threshold_local(y, block_size=7, method='gaussian') >= th)
loc_z0 = (threshold_local(z, block_size=7, method='gaussian') >= th)

### Limiar vb

#leq_b1 = (threshold_local(b, block_size=7, method='gaussian') >= vb)
loc_y1 = (threshold_local(y, block_size=7, method='gaussian') >= vb)
loc_z1 = (threshold_local(z, block_size=7, method='gaussian') >= vb)

### Limiar vg

#leq_b2 = (threshold_local(b, block_size=7, method='gaussian') >= vg)
loc_y2 = (threshold_local(y, block_size=7, method='gaussian') >= vg)
loc_z2 = (threshold_local(z, block_size=7, method='gaussian') >= vg)

### Limiar vr

#leq_b3 = (threshold_local(b, block_size=7, method='gaussian') >= vr)
loc_y3 = (threshold_local(y, block_size=7, method='gaussian') >= vr)
loc_z3 = (threshold_local(z, block_size=7, method='gaussian') >= vr)

### Limiar veqb

#leq_b4 = (threshold_local(b, block_size=7, method='gaussian') >= veqb)
loc_y4 = (threshold_local(y, block_size=7, method='gaussian') >= veqb)
loc_z4 = (threshold_local(z, block_size=7, method='gaussian') >= veqb)

### Limiar veqg

#leq_b5 = (threshold_local(b, block_size=7, method='gaussian') >= veqg)
loc_y5 = (threshold_local(y, block_size=7, method='gaussian') >= veqg)
loc_z5 = (threshold_local(z, block_size=7, method='gaussian') >= veqg)

### Limiar veqr

#leq_b6 = (threshold_local(b, block_size=7, method='gaussian') >= veqr)
loc_y6 = (threshold_local(y, block_size=7, method='gaussian') >= veqr)
loc_z6 = (threshold_local(z, block_size=7, method='gaussian') >= veqr)
