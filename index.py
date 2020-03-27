import cv2

recognise = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 15)   # Objeto reconhecedor de rosto LBPH
recognise.read("Recogniser/trainingDataLBPH.xml")