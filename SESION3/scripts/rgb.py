import cv2

img = cv2.imread('./SESION3/imagenes/1.jpeg')

# Dividimos la imagen en sus 3 canales mediante cv2.split
B, G, R = cv2.split(img)

# Volvemos a unir los 3 canales y guardamos la imagen resultante en una variable
img2 = cv2.merge((B, G, R))

# Creamos 5 ventanas para mostrar los canales de color
cv2.namedWindow('RGB', cv2.WINDOW_NORMAL)
cv2.namedWindow('R', cv2.WINDOW_NORMAL)
cv2.namedWindow('G', cv2.WINDOW_NORMAL)
cv2.namedWindow('B', cv2.WINDOW_NORMAL)
cv2.namedWindow('GBR', cv2.WINDOW_NORMAL)

# Mostramos las 5 ventanas 
cv2.imshow('RGB', img)
cv2.imshow('B', B)
cv2.imshow('G', G)
cv2.imshow('R', R)
cv2.imshow('GBR', img2)

cv2.waitKey()
cv2.destroyAllWindows()