import cv2

img = cv2.imread('./SESION3/imagenes/1.jpeg')
img2 = cv2.imread('./SESION3/imagenes/1.jpeg', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('Ventana', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('Ventana', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    key = cv2.waitKey()

    if key == ord('1'):
        cv2.imshow('Ventana', img)
    elif key == ord('2'):
        cv2.imshow('Ventana', img2)
    else:
        break

cv2.destroyAllWindows()