import cv2
import numpy as np
grating_img = cv2.imread('grating1.png')
cropped_grating = grating_img[0:255,0:255]
cv2.imwrite('cropped_img.png',cropped_grating)
#interpollating images
print(f"image shape {cropped_grating.shape}")
for i in range(4):
    j = i
    image = cropped_grating[0:255,j:j+3]
    image = cv2.resize(image,None,fx = 3,fy=1,interpolation =cv2.INTER_CUBIC)
    while(j<255):
        part_img = cropped_grating[0:255,j:j+3]
        part_img = cv2.resize(part_img,None,fx =3,fy=1,interpolation =cv2.INTER_CUBIC)
        image =cv2.hconcat([image,part_img])
        j = 3+j
    cv2.imwrite(f"{i+1}interpollated.png",image)
# for i in s
cv2.waitKey(0)
cv2.destroyAllWindows()
