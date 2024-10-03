import cv2

img = cv2.imread('./SESION3/imagenes/1.jpeg')
img2 = cv2.imread('./SESION3/imagenes/1.jpeg', cv2.IMREAD_GRAYSCALE)

while True:
    cv2.imshow('Imagen a color', img)
    cv2.imshow('Imagen a escala de grises', img2)

    key = cv2.waitKey()

    if key == ord('g'):
        cv2.imwrite('./SESION3/imagenes/imagenGuardada.png', img2)
    elif key == ord('c'):
        cv2.imwrite('./SESION3/imagenes/imagenGuardada2.png', img)
    else:
        break

cv2.destroyAllWindows()