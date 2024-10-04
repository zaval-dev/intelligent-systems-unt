import cv2

def main():
    img = cv2.imread('./SESION4/img/camaro.jpg')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV image', hsv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()