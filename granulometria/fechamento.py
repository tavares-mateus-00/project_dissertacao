
lista_estrutura = []
lista_estrutura_bin = []
lista_reconstrucao = []
lista_reconstrucao_bin = []
lista_area = []
lista_area_bin = []

import numpy as np
import cv2
import skimage.morphology as mm
import matplotlib.pyplot as plt

def abertura_residuo(a,B,Bc,tipo):
    if tipo == 'reconstrucao':
        ero = mm.dilation(a,selem=B)
        abe = np.int32(mm.reconstruction(ero,a, method='erosion', selem=Bc))
    elif tipo == 'area':
        if Bc.sum()==5:
            conec = 1
        else:
            conec = 2
        abe = mm.area_closing(a,area_threshold=B.sum(),connectivity=conec)
    else:   # caso contrario, use a abertura estrutural
        abe = mm.closing(a,selem=B)
    th = abe - a
    th_bin = 1*(th > 0)
    return th.sum(),th_bin.sum()

for imagem in lista:
    
    print(imagem)
    
    a_input = cv2.imread(imagem,1)
    ar = a_input[:,:,2]                 # canal vermelho
    ag = a_input[:,:,1]                 # canal verde
    ab = a_input[:,:,0]                 # canal azul
    a = np.int32(ar) + np.int32(ag) + np.int32(ab)
    
    Bc = np.array([[0,1,0],[1,1,1],[0,1,0]])
    iteracoes = 50
    
    abe_strut = np.zeros(iteracoes+1)
    abe_strut_bin = abe_strut.copy() 
    abe_rec = abe_strut.copy()        
    abe_rec_bin = abe_strut.copy()  
    abe_area = abe_strut.copy()      
    abe_area_bin = abe_strut.copy()
    
    raios = range(1,iteracoes+1)                                     # -> Elemento Estruturante é um disco 

    for i in raios:
        print(i)
        B = mm.disk(i)

        soma, soma_bin = abertura_residuo(a,B,Bc,'estrutural')      # Chama função crianda anteriormente
        abe_strut[i] = soma
        abe_strut_bin[i] = soma_bin

        soma, soma_bin = abertura_residuo(a,B,Bc,'reconstrucao')    # Chama função crianda anteriormente
        abe_rec[i] = soma
        abe_rec_bin[i] = soma_bin

        soma, soma_bin = abertura_residuo(a,B,Bc,'area')            # Chama função crianda anteriormente
        abe_area[i] = soma
        abe_area_bin[i] = soma_bin
        
    control_abe_strut = abe_strut.copy()
    control_abe_strut_bin = abe_strut_bin.copy()
    control_abe_rec = abe_rec.copy()
    control_abe_rec_bin = abe_rec_bin.copy()
    control_abe_area = abe_area.copy()
    control_abe_area_bin = abe_area_bin.copy()
    
    lista_estrutura.append(control_abe_strut)                   
    lista_estrutura_bin.append(control_abe_strut_bin)
    lista_reconstrucao.append(control_abe_rec)
    lista_reconstrucao_bin.append(control_abe_rec_bin)
    lista_area.append(control_abe_area)
    lista_area_bin.append(control_abe_area_bin)

np.save('fechamento_estrutura.npy',lista_estrutura)           #1
np.save('fechamento_estrutura_bin.npy',lista_estrutura_bin)   #2 
np.save('fechamento_rec.npy',lista_reconstrucao)              #3
np.save('fechamento_rec_bin.npy',lista_reconstrucao_bin)      #4
np.save('fechamento_area.npy',lista_area)                     #5
np.save('fechamento_area_bin.npy',lista_area_bin)             #6
    
