import face_recognition
import cv2
import os
import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
import time 

# a=os.path.splitext('try_list/bhunia.jpg')
# print(a)


# a=cv2.imread('try_list/bhunia.jpg')
# print(a)

# file=open("encodefile1.p","rb")
# l=pickle.load(file)
# a,b =l
# for i in a:
#     print(i)
#     print(len(i))
# print(l)

# #######################
# # Define a function to save the images of new faces
# def save_images(images, name):
#     if not os.path.exists("/Users/sujith/Desktop/dp_project/Face-Recognition-Attendance-Projects-main/Training_images"):
#         os.mkdir("/Users/sujith/Desktop/dp_project/Face-Recognition-Attendance-Projects-main/Training_images")
#     path = os.path.join("/Users/sujith/Desktop/dp_project/Face-Recognition-Attendance-Projects-main/Training_images", name)
#     if not os.path.exists(path):
#         os.mkdir(path)
#     for i, image in enumerate(images):
#         filename = os.path.join(path, f"{name}_{i}.jpg")
#         cv2.imwrite(filename, image)

# # Load the known faces and their names
# known_faces = []
# #known_names = []
# #for name in os.listdir("known_faces"):
# #    for filename in os.listdir(os.path.join("known_faces", name)):
# #       image = face_recognition.load_image_file(os.path.join("known_faces", name, filename))
# #       face_encoding = face_recognition.face_encodings(image)[0]
# #       known_faces.append(face_encoding)
# #       known_names.append(name)
        
        
# import glob
# import os
# pic_all=glob.glob(os.path.join("/Users/sujith/Desktop/dp_project/Face-Recognition-Attendance-Projects-main/Training_images", '*'))
# for i in pic_all:
#     image=face_recognition.load_image_file(i)
#     face_encoding=face_recognition.face_encodings(image)[0]
#     known_faces.append(face_encoding)
# known_names=os.listdir("/Users/sujith/Desktop/dp_project/Face-Recognition-Attendance-Projects-main/Training_images")
# known_names.remove(".DS_Store")

# # Initialize the camera
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Capture a frame from the camera
#     ret, frame = video_capture.read()

#     # Find all the faces in the frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Loop through each face in the frame
#     for face_encoding, face_location in zip(face_encodings, face_locations):
#         # Try to match the face with the known faces
#         matches = face_recognition.compare_faces(known_faces, face_encoding)
#         name = "Unknown"

#         # Find the best match
#         face_distances = face_recognition.face_distance(known_faces, face_encoding)
#         best_match_index = np.argmin(face_distances)
#         if matches[best_match_index]:
#             name = known_names[best_match_index]

#         # Draw a box around the face and label it
#         top, right, bottom, left = face_location
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#         cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 1)

#     # Display the resulting image
#     cv2.imshow("Video", frame)

#     # Wait for the user to press 'q' to quit
#     if cv2.waitKey(1000) & 0xFF == ord('q'):
#         break

#     # Allow the user to add new faces
#     if cv2.waitKey(1) & 0xFF == ord('n'):
#         name = input("Enter name: ")
#         images = []
#         for i in range(3):
#             ret, frame = video_capture.read()
#             images.append(frame)
#         save_images(images, name)

# # Release the camera and close all windows
# video_capture.release()
# cv2.destroyAllWindows()


filename="encoding_for_ic240.p"
face_pkl=open(filename,"rb")
ll=pkl.load(face_pkl)
known_data , known_names = ll
face_pkl.close()

# cam = cv2.VideoCapture(0)
# # let's assume the number of images gotten is 0
# img_counter = 0
# while True:
#     ret, frame = cam.read()
#     if not ret:
#         print('failed to grab frame')
#         break
#     cv2.imshow('test', frame)
#     #to get continuous live video feed from my laptops webcam
#     k  = cv2.waitKey(1)
#     # Here the programe waits for the key to be pressed and return the key code 
    
#     # KEY CODE OF "ESC" is 27
    
#     # KEY CODE OF "Space" is 32
    
#     # SO , Therfore if the escape key is been pressed, the app will stop
    
#     if k == 27:
#         print('escape hit, closing the app')
#         break
#     # if the spacebar key is been pressed
    
#     # screenshots will be taken
    
#     elif k  == 32:
        
#         # the format for storing the images scrreenshotted
#         img_name ="capture"+str(img_counter)+".jpg"
#         loc="/Users/sujith/Desktop/dp_project/Face-Recognition-Attendance-Projects-main/Captured/"+img_name
#         # saves the image as a png file
#         cv2.imwrite(loc, frame)
#         print('screenshot taken')
#         # the number of images automaticallly increases by 1
#         img_counter += 1

# # release the camera
# cam.release()

# # stops the camera window
# cv2.destroyAllWindows() 


fdpath="fff"
pathlist = os.listdir(fdpath)
imglist=[]

for path in pathlist:
    imglist.append(cv2.imread(os.path.join(fdpath,path)))

# known_names=os.listdir("/Users/sujith/Desktop/dp_project/Face-Recognition-Attendance-Projects-main/Training_images")
# known_names.remove(".DS_Store")



# recognised_faces=[]
# xx=0
# for img in imglist:
#     #starting counter 
#     a=time.time()
    
    
#     face_locations = face_recognition.face_locations(img)
#     b=time.time()
#     print("time taken to identify face locations "+ str(b-a))
    
    
#     face_encodings = face_recognition.face_encodings(img, face_locations,num_jitters=5)
#     c=time.time()
#     print("time taken to encode faces "+str(c-b))
#     print(" ")
    
#     img_counter=0

#     recognised_faces=[]
#     for face_encoding, face_location in zip(face_encodings, face_locations):
#         # Try to match the face with the known faces
#         matches = face_recognition.compare_faces(known_data, face_encoding,tolerance=0.5)
#         #name = "Unknown"

#         # Find the best match
#         face_distances = face_recognition.face_distance(known_data, face_encoding)
#         best_match_index = np.argmin(face_distances)
#         if matches[best_match_index]:
#             name = known_names[best_match_index]
#             recognised_faces.append(name)
#             top, right, bottom, left = face_location
#             cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
#             cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 1)
#             cv2.imshow("out",img)
#             img_name ="capture"+str(img_counter)+".jpg"
#             saved="abcd"+img_name
#             img_counter=img_counter+1
#             cv2.imwrite(saved,img)
#     # print("actual faces ")
#     # xx+=1
#     # print("recognised faces ",recognised_faces)
#     # print(" ")

# unique_faces=list(set(recognised_faces))
# print(" ")
# print(" ")
# print(unique_faces)


# im=cv2.imread("try_test/a.jpg")
# a="abcde/"+"abc.jpg"
# cv2.imwrite(a,im)
cnt=0
recognised_faces=[]
for img in imglist:
    #starting counter 
    a=time.time()

    
    face_locations = face_recognition.face_locations(img)
    b=time.time()
    print("time taken to identify face locations "+ str(b-a))
    
    
    face_encodings = face_recognition.face_encodings(img, face_locations,num_jitters=5)
    c=time.time()
    print("time taken to encode faces "+str(c-b))
    print(" ")
    img_counter=0
    for face_encoding, face_location in zip(face_encodings, face_locations):
        name="Unknown"
        # Try to match the face with the known faces
        matches = face_recognition.compare_faces(known_data, face_encoding,tolerance=0.5)
        #name = "Unknown"

        # Find the best match
        face_distances = face_recognition.face_distance(known_data, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]
            recognised_faces.append(name)
            img_counter=img_counter+1
        top, right, bottom, left = face_location
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
        cv2.imshow("out",img)

    img_name ="capture"+str(img_counter)+".jpg"
    saved="ggg/"+str(cnt)+"_"+img_name
    cnt+=1
    cv2.imwrite(saved,img)    



# import cv2
# sr = cv2.dnn_superres.DnnSuperResImpl_create()
 
# path = "EDSR_x4.pb"
 
# sr.readModel(path)
 
# sr.setModel("edsr",4)

# img = cv2.imread("try_test/b.jpeg")
 
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