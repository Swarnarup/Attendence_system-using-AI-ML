
"""
import cv2
import face_recognition
import numpy as np
import time
import os






# Loading Encoded files
import pickle

file=open('encodefile1.p','rb')
list_encode_id=pickle.load(file)
l,ids = list_encode_id
file.close()






# print(l)
# print(len(l))
# print(type(l))





group_image=cv2.imread(os.path.join("try_test",os.listdir("try_test")[0]))
group_image=cv2.cvtColor(group_image,cv2.COLOR_BGR2RGB)

print("start")

face_location=face_recognition.face_locations(group_image)
encode_current = face_recognition.face_encodings(group_image,face_location)

print("end")








p_list = []

while 1:
    tt=0
    start_tik= time.time()
    group_image=cv2.imread(os.path.join("try_test",os.listdir("try_test")[1]))
    group_image=cv2.cvtColor(group_image,cv2.COLOR_BGR2RGB)

    print("start")

    face_location=face_recognition.face_locations(group_image)
    encode_current = face_recognition.face_encodings(group_image,face_location)

    print("end")
    for i in encode_current:
        matches = face_recognition.compare_faces(l,i,tolerance=0.4)
        distance = face_recognition.face_distance(l,i)
        for i in range(len(matches)):
            if matches[i] == True:
                if ids[i] not in p_list:
                    p_list.append(ids[i])


    print(p_list)
    end_tik= time.time()

    
    if end_tik-start_tik <= 60:
        time.sleep(60-(end_tik-start_tik))
    else:
        print("time overshoot . time taken : ",end_tik-start_tik)
    

    


######################################################################

"""

def func( a ,  b ):     # a = numpy array of image using cv2.imread()
                        # b = filename of pickle file which stores dictionary["id/name"] = list([0:127]) encoding list of face of student
    import cv2
    import face_recognition
    import numpy as np
    import time
    import os

    # Loading Encoded files
    import pickle

    file=open(b,'rb')       ##########
    list_encode_id=pickle.load(file)
    l,ids = list_encode_id
    file.close()
    print(list_encode_id)

    # with open(os.path.join("try_test",os.listdir("try_test")[0]), 'rb') as f:
    #     file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
    #     group_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # group_image=cv2.imread( a )             
    group_image=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)                  ##########
    start_tik= time.time()
    print("start")

    face_location=face_recognition.face_locations(group_image)
    encode_current = face_recognition.face_encodings(group_image,face_location)
    print(face_location)
    print(encode_current)

    print("end")

    p_list = []

    for i in encode_current:
        matches = face_recognition.compare_faces(l,i)
        distance = face_recognition.face_distance(l,i)
        for i in range(len(matches)):
            if matches[i] == True:
                if ids[i] not in p_list:
                    p_list.append(ids[i])
    end_tik=time.time()
    print("time taken : ",end_tik-start_tik)
    return(p_list)


import cv2
import os

group_image=cv2.imread(os.path.join("try_test",os.listdir("try_test")[1]))
b="encodefile1.p"
print(func(group_image,b))

