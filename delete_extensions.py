from os import listdir, remove

excluidos = 0
falhas = 0

for i in listdir("D:/")[2:]:
    try:
        for j in listdir(f'D:/{i}'):
            for arq in listdir(f'D:/{i}/{j}'):
                if (arq.lower().endswith(".srt")):
                    remove(f'D:/{i}/{j}/{arq}')    
                    excluidos +=1
                    
    except:
        falhas +=1
        
print(f'Foram excluídos {excluidos} arquivos')
print(f'Houve {falhas} falhas')
