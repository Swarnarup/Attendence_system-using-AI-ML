import cv2
import face_recognition
import numpy as np
import cvzone
from cvzone.FaceDetectionModule import FaceDetector

cap=cv2.VideoCapture(1)

cap.set(3,640)
cap.set(4,480)
detector = FaceDetector()


bg=cv2.imread('frames/bg.png')
scanning=cv2.imread('frames/scanning.png')
present=cv2.imread('frames/present.png')



# Loading Encoded files
import pickle

file=open('encodefile.p','rb')
list_encode_id=pickle.load(file)
encodlist,ids = list_encode_id
file.close()
# print(type(encodlist))
# print(encodlist)


while 1:
    success , img = cap.read()

    im_resize = cv2.resize(img,(0,0),None,0.25,0.25)
    im_resize=cv2.cvtColor(im_resize,cv2.COLOR_BGR2RGB)
    
    face_location=face_recognition.face_locations(im_resize)
    encode_current = face_recognition.face_encodings(im_resize,face_location)
    # matches = face_recognition.compare_faces(encodlist,encode_current)
    # print(matches)
    # print("0",face_location)
    # print(type(face_location))
    # print(encode_current)
    # print(np.shape(encodlist))

    # print(len(encode_current))


    for encoFace , faceloc in zip(encode_current,face_location):
        print(type(encoFace))
        print(type(encodlist))
        matches = face_recognition.compare_faces(encodlist,encoFace)
        distance = face_recognition.face_distance(encodlist,encoFace)

        print("match",matches)
        print("id",distance)
        # for x in range(len(matches)):
        #     if matches[x]==True:
        #         print(ids[x])
        # y1,x2,y2,x1 = faceloc
        # y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
        # bbox=x1+50 , y1+50 , x2-x1 , y2-y1
        # # bg=cv2.rectangle(bg,(x1+50 , y1+50) , (x2-x1 , y2-y1),(0,255,0))
        # bg=cvzone.rectangle(bg,bbox,(0,255,0))

        img, bboxs = detector.findFaces(img)
        if bboxs:
            # bboxInfo - "id","bbox","score","center"
            center = bboxs[0]["center"]
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
    bg[50:50+480,50:50+640] = img
    scanning[50:50+480,50:50+640] = img
    present[50:50+480,50:50+640] = img

    cv2.imshow("frame",bg)
    cv2.waitKey(1)
