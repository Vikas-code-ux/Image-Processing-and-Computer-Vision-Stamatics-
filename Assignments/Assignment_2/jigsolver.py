import cv2
import numpy as np
import sys

input_file = sys.argv[1]
image = cv2.imread(input_file)

image_copy = image.copy()
p1 = image[0:200, 0:190, :]
p2 = image[200:410, 0:190 :]
p3 = image[150:330, 515:700, :]
p4 = image[370:421, 370:770, :]

blue = p1.copy()[:, :, 0]
green = p1.copy()[:, :, 1]
p1[:, :, 0] = green
p1[:, :, 1] = blue

p2 = np.flip(p2, 0)
p3 = np.flip(p3, 1)
p4 = np.flip(p4, 0)

p1_pad = cv2.copyMakeBorder(p1, 0, 10 ,0, 0,cv2.BORDER_REPLICATE)

image_copy[200:410, 0:190, :] = p1_pad
image_copy[0:200, 0:190, :] = p2[0:200, 0:190, :]
image_copy[150:330, 515:700, :] = p3
image_copy[370:421, 370:770, :] = p4

cv2.imshow("Jigsolved", image_copy)
status = cv2.imwrite('jigsolved.jpg', image_copy)
print("Image written to file-system : ", status)
cv2.waitKey(0)
cv2.destroyAllWindows()