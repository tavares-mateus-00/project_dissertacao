### DISSERTAÇÃO

Olá, tudo bem? Espero que sim! 

Neste projeto você encontrara o meu mestrado em Ciência da Computação.

**Autor**: $\text{Mateus Tavares}$;
**Orientador**: $\text{Franklin César Flores}$;
**Coorientador**: $\text{Yandre Maldonado e Gomes da Costa}$

**Título**: PROCESSAMENTO DE FOTOMICROGRAFIAS DE FÍGADOS DE RATOS POR MORFOLOGIA MATEMÁTICA E APRENDIZADO DE MÁQUINA.

**Universidade**: Universidade Estadual de Maringá - UEM

### $\text{Resumo}$

  Neste trabalho, são descritos resultados preliminares para a **detecção automática de câncer** (tumor Walker 256) e **dois segmentadores** que possibilitam a morfometria (extração de medidas geométricas como área e perímetro dos núcleos das células) em imagens de microfotografias pré-clínicas do tecido hepático de ratos. Na abordagem proposta para o classificador foi explorados dois tipos diferentes de descritores para capturar propriedades de textura das imagens. O primeiro descritor de textura experimentado é o _Local Phase Quantization_ (LPQ). O segundo é a técnica de Granulometria, a qual é construída por uma família de filtros morfológicos. Para classificação, fez-se uso dos algoritmos _Support Vector Machine_ (SVM), _k-Nearest Neighbor_ (k-NN) e Regressão Logística. Na abordagem proposta para a segmentação foram exploradas técnicas utilizando Processamento Digital de Imagem, Morfologia Matemática e YOLO. O **primeiro segmentador** é construído utilizando Morfologia Matemática e Processamento Digital de Imagem para segmentar os núcleos, enquanto a YOLO é utilizada para encontrar os núcleos na imagem. Já o **segundo segmentador** é construído utilizando os filtros morfológicos _Alternating Sequence Filter_ (ASF) para segmentar e encontrar os núcleos. 

### $\text{Resultado}$

Experimentos realizados em conjuntos de dados desenvolvidos pelo Laboratório de Plasticidade Neural Entérica (LPNE) da Universidade Estadual de Maringá (UEM), mostraram que ambos os descritores de textura fornecem bons resultados. No processo de **classificação**, as taxas de acurácia obtidas utilizando o classificador SVM foram de **96,67%** para o operador textura baseado em Granulometria e **91,16%** para o operador LPQ. Porém, o melhor resultado é obtido pela combinação de classificadores criados com ambos os descritores em uma estratégia de _Late Fusion_, alcançando uma acurácia de **99,16%**. O processo de classificação foi testado no conjunto de dados `data_set_`. No processo de **segmentação** o melhor resultado foi obtido com o segundo segmentador atingindo um IoU de **88,23%**. No entanto, há vícios na contagem de núcleos. O primeiro segmentador obteve um IoU de **86,36%** e uma contagem exata de núcleos. O processo de segmentação foi testado no conjunto de dados `data_set`, porém o segmentador funciona nos dois bancos de dados disponíveis. 

### $\text{LP}$

Todos os códigos foram desenvolvidos utilizando a linguagem de programação `Python`. As técnicas de Aprendizado de Máquina (AM) e de Processamento Digital de Imagens (PDI) utilizadas foram obtidas dos sítios [Sklearn](https://scikit-learn.org/stable/) e [Skimage](https://scikit-image.org/).

### $\text{Conjunto de Dados / DATA SET}$

Os conjuntos de dados utilizados neste trabalho foram criados pelos pesquisadores do LPNE da UEM. Para isso, foram utilizados ratos adultos machos, da linhagem Wistar. Todos os procedimentos envolvendo os animais foram previamente aprovados pela _Comissão Permanente de Ética em Experimentação Animal_ da UEM.

* O conjunto de dados (`data_set`) é composto por **120** microfotografias de dimensão 1024 por 768 pixels capturadas de amostras de tecido hepático dos ratos. As imagens estão divididas em duas classes: *Controle* (C) e *Tumor de Walker 256* (TW). Cada classe é formada por 60 microfotografias de seis ratos, 10 de cada rato.

* O conjunto de dados (`data_set_`) é composto por **240** microfotografias de dimensão 1024 por 768 pixels capturadas de amostras de tecido hepático dos ratos. As imagens estão divididas em quatro classes: *Controle* (C),  *Controle Tratado* (CTG), *Tumor de Walker 256* (TW) e *Tumor de Walker 256 Tratado* (TWGT). Cada classe é formada por 60 microfotografias de seis ratos, 10 cada rato.

### $\text{IMAGEM RESULTANTE}$

![Resultado do método 1](https://github.com/mafta-00/project_dissertacao/blob/main/image_results/ct-seg-primeira.png)

### $\text{CITAÇÃO}$

* $\text{Classificação}$
```
@Article{a15080268,
AUTHOR = {Carvalho, Mateus F. T. and Silva, Sergio A. and Bernardo, Carla Cristina O. and Flores, Franklin César and Perles, Juliana Vanessa C. M. and Zanoni, Jacqueline Nelisis and Costa, Yandre M. G.},
TITLE = {Cancer Identification in Walker 256 Tumor Model Exploring Texture Properties Taken from Microphotograph of Rats Liver},
JOURNAL = {Algorithms},
VOLUME = {15},
YEAR = {2022},
NUMBER = {8},
ARTICLE-NUMBER = {268},
URL = {https://www.mdpi.com/1999-4893/15/8/268},
ISSN = {1999-4893},
DOI = {10.3390/a15080268}
}
```
* $\text{Segmentação}$
```
@INPROCEEDINGS{10634016,
  author={Flores, Franklin C. and Carvalho, Mateus F. T. and Da Silva, Sergio A. and Berton, Leandro E. F. and Bernardo, Carla C. O. and Sevilha, André L. R. G. and Perles, Juliana V. C. M. and Zanoni, Jacqueline N. and Felipe, Gustavo Z. and Costa, Yandre M. G.},
  booktitle={2024 31st International Conference on Systems, Signals and Image Processing (IWSSIP)}, 
  title={Segmentation of Hepatocytes Nuclei Using YOLO and Mathematical Morphology}, 
  year={2024},
  volume={},
  number={},
  pages={1-7},
  keywords={YOLO;Image segmentation;Digital images;Area measurement;Morphology;Liver;Rats;Alternating sequential filter;Mathematical morphology;segmentation;YOLO;liver tissue},
  doi={10.1109/IWSSIP62407.2024.10634016}}
```

$\text{Divirta-se!!!}$ 😁
