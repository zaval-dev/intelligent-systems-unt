import cv2
import numpy as np

img = cv2.imread('./SESION3/imagenes/candados.jpg')

rows, cols, channels = img.shape
print(rows, cols, channels)

candado1 = img[0:rows, 0:cols//2]
candado2 = img[0:rows, cols//2:]

imagenCompuesta = np.zeros((rows, cols, 3), np.uint8)

rows, cols, channels = imagenCompuesta.shape

imagenCompuesta[0:rows, 0:cols//2]
imagenCompuesta[0:rows, cols//2:]

cv2.imshow('original', img)
cv2.imshow('candado1', candado1)
cv2.imshow('candado2', candado2)
cv2.imshow('compuesta', imagenCompuesta)

cv2.waitKey()
cv2.destroyAllWindows()