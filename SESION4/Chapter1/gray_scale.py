import cv2

def main():
    img = cv2.imread('./SESION4/img/camaro.jpg', 0)
    cv2.imshow('Imagen a blanco y negro', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()