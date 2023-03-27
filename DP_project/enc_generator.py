import cv2
import os
import pickle
import face_recognition


fdpath="try_list"
pathlist = os.listdir(fdpath)
imglist=[]
id_list=[]

for path in pathlist:
    imglist.append(cv2.imread(os.path.join(fdpath,path)))
    id_list.append(os.path.splitext(path)[0])
print(id_list)


def findencoding(imglist1):
    enclist=[]
    for img in imglist1:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        enc= face_recognition.face_encodings(img)[0]
        enclist.append(enc)
    return enclist

print("enc started")
encodelist_savd=findencoding(imglist)

list_encode_id = [encodelist_savd,id_list]
print("enc ended")

file =  open("encodefile1.p",'wb')
pickle.dump(list_encode_id,file)
file.close()

print("file saved")
