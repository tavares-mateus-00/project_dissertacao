import xlsxwriter

planilha = xlsxwriter.Workbook('imagem.xlsx') # Nome do arquivo .xlsx
zona = planilha.add_worksheet('imagem_x')     # Nome da planilha

linha, coluna = 1,1

#zona.write(linha,coluna,'Quantidade de Núcleos na Imagem')
#zona.write(luna,coluna+1,len(p))

#zona.write(linha+1,coluna,'Quantidade de Núcleos segmentados')
#zona.write(linha+1,coluna,len())

zona.write(linha+3,coluna,'Núcleo')
zona.write(linha+3,coluna+1,'Área')
zona.write(linha+3,coluna+2,'Perímetro')

linha1 = linha+4

for i in range(len(p)):
    zona.write(linha1+i, coluna, i)
    zona.write(linha1+i, coluna+1, area[i])
    zona.write(linha1+i, coluna+2, perimetro[i])

planilha.close()
