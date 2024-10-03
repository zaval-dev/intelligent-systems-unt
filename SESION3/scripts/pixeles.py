import cv2
import numpy as np

imagenObscura = np.zeros((100,100,3), np.uint8)

pixel = imagenObscura[97,97]

print(pixel)

imagenObscura[30,60] = [255,255,255]

print(pixel)

# Obtenemos filas, columnas y canales mediante el método shape
rows, cols, channels = imagenObscura.shape
print(rows, cols, channels)

# Recorremos la imagen imprimiendo los valores de cada pixel
# for i in range(rows):
#     for j in range(cols):
#         print(imagenObscura[i,j])

# Modificar los valores de cada pixel
for i in range(rows):
    for j in range(cols):
        pixel = imagenObscura[i,j]
        if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            imagenObscura[i,j] = [125,125,200]

cv2.namedWindow('black', cv2.WINDOW_NORMAL)
cv2.imshow('black', imagenObscura)

cv2.waitKey()
cv2.destroyAllWindows()