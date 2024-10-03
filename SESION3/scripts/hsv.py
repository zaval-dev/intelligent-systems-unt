import cv2

img = cv2.imread('./SESION3/imagenes/1.jpeg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('HSV', hsv)
cv2.imshow('H', h)
cv2.imshow('S', s)
cv2.imshow('V', v)

cv2.imshow('Gray', img2)

cv2.waitKey()

cv2.destroyAllWindows()