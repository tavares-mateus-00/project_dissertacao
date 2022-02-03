controle = ['controle (1).jpg', 'controle (2).jpg', 'controle (3).jpg',
            'controle (4).jpg', 'controle (5).jpg', 'controle (6).jpg',
            'controle (7).jpg', 'controle (8).jpg', 'controle (9).jpg',
            'controle (10).jpg', 'controle (11).jpg', 'controle (12).jpg',
            'controle (13).jpg', 'controle (14).jpg', 'controle (15).jpg',
            'controle (16).jpg', 'controle (17).jpg', 'controle (18).jpg',
            'controle (19).jpg', 'controle (20).jpg', 'controle (21).jpg',
            'controle (22).jpg', 'controle (23).jpg', 'controle (24).jpg',
            'controle (25).jpg', 'controle (26).jpg', 'controle (27).jpg',
            'controle (28).jpg', 'controle (29).jpg', 'controle (30).jpg',
            'controle (31).jpg', 'controle (32).jpg', 'controle (33).jpg',
            'controle (34).jpg', 'controle (35).jpg', 'controle (36).jpg',
            'controle (37).jpg', 'controle (38).jpg', 'controle (39).jpg',
            'controle (40).jpg', 'controle (41).jpg', 'controle (42).jpg',
            'controle (43).jpg', 'controle (44).jpg', 'controle (45).jpg',
            'controle (46).jpg', 'controle (47).jpg', 'controle (48).jpg',
            'controle (49).jpg', 'controle (50).jpg', 'controle (51).jpg',
            'controle (52).jpg', 'controle (53).jpg', 'controle (54).jpg',
            'controle (55).jpg', 'controle (56).jpg', 'controle (57).jpg',
            'controle (58).jpg', 'controle (59).jpg', 'controle (60).jpg']

tw = ['tw (1).jpg','tw (2).jpg','tw (3).jpg',
      'tw (4).jpg','tw (5).jpg','tw (6).jpg',
      'tw (7).jpg','tw (8).jpg','tw (9).jpg',
      'tw (10).jpg','tw (11).jpg','tw (12).jpg',
      'tw (13).jpg','tw (14).jpg','tw (15).jpg',
      'tw (16).jpg','tw (17).jpg','tw (18).jpg',
      'tw (19).jpg','tw (20).jpg','tw (21).jpg',
      'tw (22).jpg','tw (23).jpg','tw (24).jpg',
      'tw (25).jpg','tw (26).jpg','tw (27).jpg',
      'tw (28).jpg','tw (29).jpg','tw (30).jpg',
      'tw (31).jpg','tw (32).jpg','tw (33).jpg',
      'tw (34).jpg','tw (35).jpg','tw (36).jpg',
      'tw (37).jpg','tw (38).jpg','tw (39).jpg',
      'tw (40).jpg','tw (41).jpg','tw (42).jpg',
      'tw (43).jpg','tw (44).jpg','tw (45).jpg',
      'tw (46).jpg','tw (47).jpg','tw (48).jpg',
      'tw (49).jpg','tw (50).jpg','tw (51).jpg',
      'tw (52).jpg','tw (53).jpg','tw (54).jpg',
      'tw (55).jpg','tw (56).jpg','tw (57).jpg',
      'tw (58).jpg','tw (59).jpg','tw (60).jpg']

lista = controle + tw
"""

lista = ['controle (34).jpg']

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
    
