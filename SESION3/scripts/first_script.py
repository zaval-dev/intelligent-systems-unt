import cv2

# Leer una imagen con ruta relativa
img = cv2.imread('./SESION3/imagenes/1.jpeg')

# Mostrar la imagen en una ventana
cv2.imshow('Ventana', img)

cv2.waitKey()
cv2.destroyAllWindows()

# Escribir una imagen en cierta ruta
cv2.imwrite('./SESION3/imagenes/nuevaImagen.jpeg', img)