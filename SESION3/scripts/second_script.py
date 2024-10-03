import cv2

img = cv2.imread('./SESION3/imagenes/1.jpeg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Imagen en escala de grises', img)

cv2.waitKey()

cv2.destroyAllWindows()

cv2.imwrite('./SESION3/imagenes/ImagenGrises.jpeg', img)