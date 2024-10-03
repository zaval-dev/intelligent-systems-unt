import cv2

img = cv2.imread('./SESION3/imagenes/1.jpeg')
img2 = cv2.imread('./SESION3/imagenes/1.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Imagen a color', img)

while True:
    # cv2.imshow('Imagen a escala de grises', img2)

    key = cv2.waitKey()

    if key == ord('1'):
        cv2.destroyAllWindows()
        cv2.imshow('Color image', img)
    elif key == ord('2'):
        cv2.destroyAllWindows()
        cv2.imshow('GrayScale image', img2)
    else:
        break
cv2.destroyAllWindows()