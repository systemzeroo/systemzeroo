# COLETA DADOS NO LBPH EXECUTANDO-O EM UMA IMAGEM DADA E SALVANDO DADOS EM UM ARQUIVO DE TEXTO 
# SALVAR OS DADOS EM 3 ARQUIVOS DE TEXTO E ENVIAR OS DADOS 

import os               # importando o SO para o caminho
import cv2              # importando a biblioteca OpenCV
import numpy as np      # importando a biblioteca Numpy
from PIL import Image   # importando Biblioteca de imagens
import matplotlib.pyplot as plt # Importando biblioteca de plotagem
import NameFind

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
path = 'dataSet'  # caminho para as fotos

img = cv2.imread('Me4.jpg')  # -------------->>>>>>>>>>>>>>>>>>  A imagem a ser verificada

def getImageWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []

    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')       # Abrir imagem e converter para cinza
        print(str((faceImage.size)))
        faceImage = faceImage.resize((110, 110))             # redimensionar a imagem
        faceNP = np.array(faceImage, 'uint8')                # converter a imagem em matriz Numpy
        print(str((faceNP.shape)))
        ID = int(os.path.split(imagePath)[-1].split('.')[1]) # GObter o ID da matriz
        FaceList.append(faceNP)                              # Anexar a matriz Numpy à lista
        IDs.append(ID)                                       # Anexe o ID à lista de IDs

    return np.array(IDs), FaceList     # Os IDs são convertidos em uma matriz Numpy

face_number = 1
IDs, FaceList = getImageWithID(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                   # Converta a câmera em cinza
faces = face_cascade.detectMultiScale(gray, 1.3, 4)            # Detecte os rostos e armazene as posições
radTrain = open("SaveData/LBPH/LBPH_PIXEL_RADIUS.txt", "w+")   # abra o arquivo para gravar dados
neiTrain = open("SaveData/LBPH/LBPH_NEIGHBOURS.txt", "w+")     # abra o arquivo para gravar dados
cellTrain = open("SaveData/LBPH/LBPH_CELLS.txt", "w+")         # abra o arquivo para gravar dados

for (x, y, w, h) in faces:
    Face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))
    radPix = 1
    rad_tabal_ID = []
    rad_tabal_conf = []
    # --------------------------- Execute testes para o raio do centro ----------------
    for _ in range(54):
        recog = cv2.face.LBPHFaceRecognizer_create(radPix)  # criando o EIGEN FACE RECOGNISER
        print('TRAINING FOR  ' + str(radPix) + ' PIXELS FROM CENTRE')
        recog.train(FaceList, IDs)           # O reconhecedor é treinado usando as imagens
        print('LBPH FACE RECOGNISER TRAINED')
        ID, conf = recog.predict(Face)
        rad_tabal_ID.append(ID)
        rad_tabal_conf.append(conf)
        radTrain.write(str(ID) + "," + str(conf) + "\n")
        print ("FOR RADIUS: " + str(radPix) + " ID IS: " + str(ID) + " THE CONFIDENCE: " + str(conf))
        radPix = radPix + 1
    # ---------------------------------------- 1ª PARTE ----------------------------------
    plt.subplot(2, 1, 1)
    plt.plot(rad_tabal_ID)
    plt.title('ID against Pixel Radius', fontsize=10)
    plt.axis([0, radPix, 0, 25])
    plt.ylabel('ID', fontsize=8)
    plt.xlabel('Radius (Pixels)', fontsize=8)
    p2 = plt.subplot(2, 1, 2)
    plt.plot(rad_tabal_conf, 'red')
    plt.title('Confidence against Pixel Radius', fontsize=10)
    p2.set_xlim(xmin=0)
    p2.set_xlim(xmax=radPix)
    plt.ylabel('Confidence', fontsize=8)
    plt.xlabel('Radius (Pixels)', fontsize=8)
    plt.tight_layout()
    plt.show()
    # ---------------------------  Execute testes para os vizinhos -----------------------------
    radPixel = input('ENTER THE IDEAL PIXEL RADIUS ') # MUDE O RAIO PIXEL SE UM VALOR MELHOR É ENCONTRADO
    neighbour = 1
    nei_ID = []
    nei_conf = []
    for _ in range(13):
        recog = cv2.face.createLBPHFaceRecognizer(radPixel, neighbour) # Criando o Reconhecimento Facial
        print('TRAINING FOR  ' + str(neighbour) + ' NEIGHBOURS')
        recog.train(FaceList, IDs) # O reconhecedor é treinado usando as imagens
        print('LBPH FACE RECOGNISER TRAINED')
        ID, conf = recog.predict(Face)
        nei_ID.append(ID)
        nei_conf.append(conf)
        neiTrain.write(str(ID) + "," + str(conf) + '\n')
        print ('FOR RADIUS: ' + str(radPixel) + " AND " + str(neighbour) + "NEIGHBOURS, ID IS: " + str(ID) + " THE CONFIDENCE: " + str(conf))
        neighbour = neighbour + 1
    # ---------------------------------------- 2º PLOT -----------------------------------------------------
    plt.subplot(2, 1, 1)
    plt.plot(nei_ID)
    plt.title('ID against number of neighbours', fontsize=10)
    plt.axis([0, neighbour, 10, 25])
    plt.ylabel('ID', fontsize=8)
    plt.xlabel('Number of neighbours', fontsize=8)
    p2 = plt.subplot(2, 1, 2)
    plt.plot(nei_conf, 'red')
    plt.title('ID against number of neighbours', fontsize=10)
    p2.set_xlim(xmin=0)
    p2.set_xlim(xmax=neighbour)
    plt.ylabel('Confidence', fontsize=8)
    plt.xlabel('Number of neighbours', fontsize=8)
    plt.tight_layout()
    plt.show()
    # --------------------------- Execute testes para o número da célula -----------------------------
    neighbour = input('ENTER THE IDEAL NUMBER OF NEIGHBOURS ')# MUDE O PRÓXIMO SE O MELHOR VALOR É ENCONTRADO
    cellVal = 1
    cell_ID = []
    cell_conf = []
    for _ in range(50):
        recog = cv2.face.createLBPHFaceRecognizer(radPixel, neighbour, cellVal, cellVal)  # Criando o Reconhecimento Facial
        print('TRAINING FOR  ' + str(cellVal) + ' CELLS')
        recog.train(FaceList, IDs) # O reconhecedor é treinado usando as imagens
        print('LBPH FACE RECOGNISER TRAINED')
        ID, conf = recog.predict(Face)
        cell_ID.append(ID)
        cell_conf.append(conf)
        cellTrain.write(str(ID) + "," + str(conf) + "\n")
        print ('FOR RADIUS: ' + str(radPixel) + " , " + str(neighbour) + "NEIGHBOURS AND CELL VALUE " + str(cellVal) + ", ID IS: " + str(ID) + " THE CONFIDENCE: " + str(conf))
        cellVal = cellVal + 1
    NameFind.tell_time_passed()

    # ------------------------------------------- TODOS OS SEIS LOTES -------------------------------
    plt.subplot(3, 2, 1)
    plt.plot(rad_tabal_ID)
    plt.title('ID against Pixel Radius', fontsize=10)
    plt.axis([0, 53, 0, 25])
    plt.ylabel('ID', fontsize=8)
    plt.xlabel('Radius (Pixels)', fontsize=8)
    plt.subplot(3, 2, 2)
    plt.plot(rad_tabal_conf, 'red')
    plt.title('Confidence against Pixel Radius', fontsize=10)
    plt.ylabel('Confidence', fontsize=8)
    plt.xlabel('Radius (Pixels)', fontsize=8)
    plt.subplot(3, 2, 3)
    plt.plot(nei_ID)
    plt.title('ID against number of neighbours', fontsize=10)
    plt.axis([0, 12, 10, 25])
    plt.ylabel('ID', fontsize=8)
    plt.xlabel('Number of neighbours', fontsize=8)
    plt.subplot(3, 2, 4)
    plt.plot(nei_conf, 'red')
    plt.title('ID against number of neighbours', fontsize=10)
    plt.ylabel('Confidence', fontsize=8)
    plt.xlabel('Number of neighbours', fontsize=8)
    plt.subplot(3, 2, 5)
    plt.plot(cell_ID)
    plt.title('ID against number of cells', fontsize=10)
    plt.axis([0, 49, 0, 25])
    plt.ylabel('ID', fontsize=8)
    plt.xlabel('Number of Cells', fontsize=8)
    plt.subplot(3, 2, 6)
    plt.plot(cell_conf, 'red')
    plt.title('ID against number of cells', fontsize=10)
    plt.ylabel('Confidence', fontsize=8)
    plt.xlabel('Number of Cells', fontsize=8)
    plt.tight_layout()
    plt.show()
    
    face_number = face_number + 1

radTrain.close()
neiTrain.close()
cellTrain.close()
cv2.destroyAllWindows()