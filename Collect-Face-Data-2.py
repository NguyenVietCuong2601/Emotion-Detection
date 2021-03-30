import  numpy as np
import cv2
from matplotlib import pyplot as plt
import os

directory_src='Data\\train\\Calm\\'
directory_data='Data\\train\\Calm\\'
new_width=325
new_height=260
dsize=(new_width, new_height)
count=0
for image_indexed in os.listdir(directory_src):
    img = cv2.imread(directory_src + image_indexed)
    output=(cv2.resize(img, dsize))
    _,roi=cv2.threshold(output, 80, 255, cv2.THRESH_BINARY)
    cv2.imwrite(directory_data + str(count) + '.jpg', roi)
    count+=1
    print(str(count)+'.ipg')
#cv2.imshow('image',roi)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


