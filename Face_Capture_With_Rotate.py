# -------------------- ISTO É USADO PARA CAPTURAR A LOJA DAS FOTOS PARA TREINAR OS SISTEMAS DE RECONHECIMENTO DE ROSTO ------------------
# ------------ ADICÇÕES ESPECIAIS SÃO FEITAS PARA SALVAR IMAGENS APENAS COM ILUMINAÇÃO CORRETA E CABEÇAS INCLINADAS CORRETAS---------
# ------------------------------ CREATED BY LAHIRU DINALANKARA - AKA SPIKE ---------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

import cv2                  # Importando o opencv
import numpy as np          # Importar Python Numarical
import NameFind           # Importar Função NameFind

WHITE = [255, 255, 255]

# Importar as cascatas de Haar para detecção de rosto

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml') # Classificador "face frontal" Haar Cascade
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml') # Classificador "olho" Haar Cascade

ID = NameFind.getId()
cap = cv2.VideoCapture(0)                                                                           # Camera object
Count = 0

while Count < 50:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converta a câmera em grayScale

    if np.average(gray) > 110: # Testando o brilho da imagem
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detecte os rostos e armazene as posições
        for (x, y, w, h) in faces:  # Quadros LOCALIZAÇÃO X, LARGURA Y, ALTURA
            FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)] # O rosto é isolado e cortado
            Img = (NameFind.DetectEyes(FaceImage))
            cv2.putText(gray, "FACE DETECTADA", (x+int((w/2)), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
            if Img is not None:
                frame = Img     # Mostrar os rostos detectados
            else:
                frame = gray[y: y+h, x: x+w]
            cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", frame)
            cv2.waitKey(300)
            cv2.imshow("CAPTURED PHOTO", frame)  # mostra a imagem capturada
            Count = Count + 1
    cv2.imshow('Face Recognition System Capture Faces', gray)  # Mostrar o vídeo
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
print ('FACE CAPTURE FOR THE SUBJECT IS COMPLETE')

import Trainer_All
import Tela3

cap.release()
cv2.destroyAllWindows()