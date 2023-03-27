import cv2
import face_recognition
import numpy as np
import time

# l=[]

# bhunia=cv2.imread('try_list/bhunia.jpg')
# aman=cv2.imread('try_list/aman.jpg')
# sujit=cv2.imread('try_list/sujit.jpg')

# print("start")

# bhunia_1=cv2.cvtColor(bhunia,cv2.COLOR_BGR2RGB)
# enc_bh= face_recognition.face_encodings(bhunia_1)[0]
# l.append(enc_bh)

# aman_1=cv2.cvtColor(aman,cv2.COLOR_BGR2RGB)
# enc_am= face_recognition.face_encodings(aman_1)[0]
# l.append(enc_am)

# sujit_1=cv2.cvtColor(sujit,cv2.COLOR_BGR2RGB)
# enc_sj= face_recognition.face_encodings(sujit_1)[0]
# l.append(enc_sj)

# print("end")



# Loading Encoded files
import pickle

file=open('encodefile1.p','rb')
list_encode_id=pickle.load(file)
l,ids = list_encode_id
file.close()



# print(l)
# print(len(l))
# print(type(l))

group1=cv2.imread('try_test/group1.jpg')
group1=cv2.cvtColor(group1,cv2.COLOR_BGR2RGB)
group2=cv2.imread('try_test/group2.jpeg')
group2=cv2.cvtColor(group2,cv2.COLOR_BGR2RGB)
print("start")

face_location=face_recognition.face_locations(group1)
encode_current = face_recognition.face_encodings(group1,face_location)

print("end")

print("start")

face_location2=face_recognition.face_locations(group2)
encode_current2 = face_recognition.face_encodings(group2,face_location2)

print("end")

# print(face_location)
# print(encode_current)

# print(len(encode_current))
# print(np.shape(encode_current))
# print(type(encode_current))


# print(len(encoface))
# print(np.shape(encoface))
# print(type(encoface))


# enc= face_recognition.face_encodings(img)[0]

# for i in l:
#     matches = face_recognition.compare_faces(encode_current,i)
#     distance = face_recognition.face_distance(encode_current,i)

#     print("match",matches)
#     print("id",distance)

# for encoFace , faceloc in zip(encode_current,face_location):
#         print(type(encoFace))
#         print(type(l))
#         matches = face_recognition.compare_faces(l,encoFace)
#         distance = face_recognition.face_distance(l,encoFace)

#         print("match",matches)
#         print("id",distance)

p_list = []
for i in encode_current:
    matches = face_recognition.compare_faces(l,i,tolerance=0.4)
    distance = face_recognition.face_distance(l,i)
    for i in range(len(matches)):
        if matches[i] == True:
            p_list.append(ids[i])
for i in encode_current2:
    matches = face_recognition.compare_faces(l,i,tolerance=0.4)
    distance = face_recognition.face_distance(l,i)
    for i in range(len(matches)):
        if matches[i] == True:
            p_list.append(ids[i])
print(p_list)

for i in range(100):
    img=cv2.c
