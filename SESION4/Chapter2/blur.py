import cv2
import numpy as np

def apply_and_show_fliter(img, kernel, window_name):
    output = cv2.filter2D(img, -1, kernel)
    cv2.imshow(window_name, output)
  
img = cv2.imread('./SESION4/img/camaro.jpg')

kernels = {
    "Identity kernel" : np.array([[0,0,0], [0,1,0], [0,0,0]]),
    "3x3 kernel": np.ones((3,3), np.float32) / 9.0
}

cv2.imshow('Original image', img)

for key, kernel in kernels.items():
    apply_and_show_fliter(img, kernel, key)
    
cv2.waitKey(0)
cv2.destroyAllWindows()