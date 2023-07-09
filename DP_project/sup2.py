import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("abc.jpg")
sr = cv2.dnn_superres.DnnSuperResImpl_create()
path = "FSRCNN_x3.pb"
 
sr.readModel(path)
 
sr.setModel("fsrcnn",3)
 
result = sr.upsample(img)
# cv2.imshow("ghgv",result)
 
# Resized image
resized = cv2.resize(img,dsize=None,fx=3,fy=3)
# cv2.imshow("ghgv",resized)
# cv2.waitKey(0)
# plt.figure(figsize=(12,8))
# plt.subplot(1,3,1)
# # Original image
# plt.imshow(img[:,:,::-1])
# plt.subplot(1,3,2)
# # SR upscaled
# plt.imshow(result[:,:,::-1])
# plt.subplot(1,3,3)
# # OpenCV upscaled
# plt.imshow(resized[:,:,::-1])
# plt.show()
cv2.imwrite("try_test/i"+str(50)+"ac.jpg",resized)

# sr = cv2.dnn_superres.DnnSuperResImpl_create()
 
# path = "EDSR_x4.pb"
 
# sr.readModel(path)
 
# sr.setModel("edsr",4)
 
# result = sr.upsample(img)
 
# # Resized image
# resized = cv2.resize(img,dsize=None,fx=4,fy=4)
 
# plt.figure(figsize=(12,8))
# plt.subplot(1,3,1)
# # Original image
# plt.imshow(img[:,:,::-1])
# plt.subplot(1,3,2)
# # SR upscaled
# plt.imshow(result[:,:,::-1])
# plt.subplot(1,3,3)
# # OpenCV upscaled
# plt.imshow(resized[:,:,::-1])
# plt.show()

# gb=cv2.GaussianBlur(img,(7,7),2)
# adw=cv2.addWeighted(img,1.5,gb,-0.5,0)

# cv2.imshow("org",img)
# cv2.imshow("gb",gb)
# cv2.imshow("awd",adw)
# cv2.waitKey(0)



# import picamera
# import time

# isol=[100,400,600,800]
# sh=[-50,0,50]
# sat=[-50,0,50]
# cont=[-50,0,50]
# brt=[0,50,80]

# camera = picamera.PiCamera(resolution=(1920,1080))
# #camera.capture_sequence()
# for i in isol:
#     camera.iso=i
#     for j in sh:
#         camera.sharpness=j
#         for k in sat:
#             camera.saturation=k
#             for l in cont:
#                 camera.contrast=l
#                 for m in brt:
#                     camera.brightness=m
#                     camera.capture("ISO_"+str(i)+"sharpness_"+str(j)+"saturation_"+str(k)+"contrast_"+str(l)+"brightness_"+str(m)+'.jpg')


