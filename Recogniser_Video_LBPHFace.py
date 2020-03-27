#   RECONHECEDOR DO RECONHECEDOR LBPH FACE 
#   PARA O RECONHECIMENTO FACIAL, TODAS AS CARAS SÃO NECESSÁRIAS DE MESMO TAMANHO 

import cv2                  # Importando o opencv
import numpy as np          # Importar Python Numarical
import NameFind
import webbrowser
  
# Importe as cascatas de Haar para obter a detecção de rosto e olho

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

recognise = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 15)   # Objeto reconhecedor de rosto LBPH
recognise.read("Recogniser/trainingDataLBPH.xml")
  # Carregue os dados de treinamento do treinador para reconhecer os rostos
# -------------------------  INICIAR A ALIMENTAÇÃO DE VÍDEO ------------------------------------------

cap = cv2.VideoCapture(0)                 # Objeto da câmera
# cap = cv2.VideoCapture('TestVid.wmv')   # Objeto de vídeo

while True:
    ret, img = cap.read()                               # Leia o objeto da câmera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # Converta a câmera em cinza
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detecte os rostos e armazene as posições
    
    for (x, y, w, h) in faces:    # Quadros LOCALIZAÇÃO X, LARGURA Y, ALTURA
        
        # Os olhos devem estar dentro do rosto.
        gray_face = gray[y: y+h, x: x+w]                # O rosto é isolado e cortado
        eyes = eye_cascade.detectMultiScale(gray_face)
        for (ex, ey, ew, eh) in eyes:
            ID, conf = recognise.predict(gray_face)     # Determine o ID da foto
            # NAME = NameFind.ID2Name(ID, conf)
            # NameFind.DispID(x, y, w, h, NAME, gray)
            if conf < 7:
                NAME = NameFind.ID2Name(ID, conf)
                NameFind.DispID(x, y, w, h, NAME, gray)
            else:
                NameFind.DispID(x, y, w, h,
                
                 "NAO RECONHECIDO ", gray)
        
        Nome = NameFind.NOME(ID)

        if Nome == Nome:
            if cv2.waitKey(1) & 0xFF == ord('o'): # A tecla 'o' abre o navegador !!
                NameFind.AbrirURL(ID)
                break

    cv2.imshow('LBPH Face Recognition System', gray)   # Mostrar o vídeo
    
    if cv2.waitKey(1) & 0xFF == ord('q'):              # Saia se a chave for Q
        break

cap.release()
cv2.destroyAllWindows()
