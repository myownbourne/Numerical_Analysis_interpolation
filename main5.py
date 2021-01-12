from image_resize import *
import time
img=cv2.imread("test.jpg",0).astype(np.float)

time_start1=time.time()
out=bilinear(img,2,2).astype(np.uint8)
time_end1=time.time()
time1=time_end1-time_start1

time_start2=time.time()
out2=NN(img,2,2).astype(np.uint8)
time_end2=time.time()
time2=time_end2-time_start2


img_ori=cv2.imread("test.jpg",0)
cv2.imshow('ori',img_ori)
cv2.imshow("Bilinear", out)
cv2.imshow("Nearest Neighbor", out2)

print()
print('computational complexity of 2 method in s')
print()
print('Bilinear  Nearest_Neighbor')
print('----------------------------')
print('%f' %time1,'   ','%f' %time2)
print('----------------------------')


cv2.waitKey(0)
cv2.destroyAllWindows()