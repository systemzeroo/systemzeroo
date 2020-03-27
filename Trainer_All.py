# --------------------------TREINADOR PARA TODOS OS ALGORITMOS NO RECONHECIMENTO FACIAL ----------------

import os                 # importando o SO para o caminho(pasta)
import cv2                # importando a biblioteca OpenCV
import numpy as np        # importando a biblioteca Numpy
from PIL import Image     # importando Biblioteca de imagens


LBPHFace = cv2.face.LBPHFaceRecognizer_create(1, 1, 7,7) # Criar LBPH FACE RECOGNISER

path = 'dataSet'                                        # caminho para as fotos
def getImageWithID (path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    FaceList = []
    IDs = []
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')  # Abrir imagem e converter para cinza
        faceImage = faceImage.resize((110,110))  # redimensionar a imagem para que o reconhecedor EIGEN possa ser treinado
        faceNP = np.array(faceImage, 'uint8')    # converter a imagem em matriz Numpy
        ID = int(os.path.split(imagePath)[-1].split('.')[1]) # Recrie novamente o ID da matriz
        FaceList.append(faceNP)                         # Anexar a matriz Numpy à lista
        IDs.append(ID)                                  # Anexe o ID à lista de IDs
        cv2.imshow('Training Set', faceNP)              # Mostrar as imagens na lista
        cv2.waitKey(1)
    return np.array(IDs), FaceList                      # Os IDs são convertidos em uma matriz Numpy
IDs, FaceList = getImageWithID(path)

# ------------------------------------ TREINANDO O RECONHECEDOR ----------------------------------------
print('TREINANDO......')
LBPHFace.train(FaceList, IDs)
LBPHFace.save('Recogniser/trainingDataLBPH.xml')
print('TREINAMENTO COMPLETO......')

cv2.destroyAllWindows()