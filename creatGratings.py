import numpy as np
import cv2

my_img_3 = np.zeros((255, 255, 3), dtype = "uint8")
my_img_3.fill(255)
image = my_img_3
# image2 = my_img_3
# cv2.imshow('3 Channel Window', my_img_3)
# cv2.imshow("image2_initail_1",image2)

i=0
start_point = (i,0)
end_point=(i,255)
while(i<255):
    image = cv2.line(image, start_point, end_point,(0,0,0),2)
    i=i+4
    start_point = (i,0)
    end_point = (i,255)
cv2.imshow("image1_final",image)
# cv2.imshow("image2_initail",image2)
image2 = np.zeros((255,255,3),dtype="uint8")
image2.fill(255)
j=0
start_point = (1,0)
end_point=(1,255)
while(j<255):
    image2 = cv2.line(image2, start_point, end_point,(0,0,0),2)
    j=j+4
    start_point = (j,0)
    end_point = (j,255)

cv2.imshow("image2_final",image2)
# cv2.imshow("image",my_img_3)

cv2.waitKey(0)
cv2.destroyAllWindows()
