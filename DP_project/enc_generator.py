import cv2
import os
import pickle
import face_recognition


fdpath="2nd_year"
pathlist = os.listdir(fdpath)
imglist=[]
id_list=[]

for path in pathlist:
    imglist.append(cv2.imread(os.path.join(fdpath,path)))
    id_list.append(os.path.splitext(path)[0])
print(id_list)
print(len(id_list))


def findencoding(imglist1):
    enclist=[]
    i=0
    for img in imglist1:
        print("count : ",i)
        i+=1
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        enc= face_recognition.face_encodings(img)[0]
        enclist.append(enc)
        print("done")
    return enclist

print("enc started")
encodelist_savd=findencoding(imglist)

list_encode_id = [encodelist_savd,id_list]
print("enc ended")

file =  open("encoding_2ndYear.p",'wb')
pickle.dump(list_encode_id,file)
file.close()

print("file saved")


# def appending_fn(path_l,image_path,str_to_remove):

#     img = cv2.imread(image_path)

#     file=open(path_l,'rb')
#     list_encode_id=pickle.load(file)
#     l,ids = list_encode_id

#     if os.path.splitext(image_path)[0][len(str_to_remove)+2:] not in ids:
#         print("enc started")
#         img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         encd = face_recognition.face_encodings(img)[0]
#         print("enc ended")

#         l.append(encd)
#         ids.append(os.path.splitext(image_path)[0][len(str_to_remove)+2:])
#         list_encode_id = [l,ids]

        
    
#     else:
#         print("data exists")
    
#     file =  open("encodefile1.p",'wb')
#     pickle.dump(list_encode_id,file)
#     file.close()

#     print("file saved")

# # file=open('encodefile1.p','rb')
# # list_encode_id=pickle.load(file)
# for i in range(12):
#     appending_fn('encodefile1.p',os.path.join("training_images",os.listdir("training_images")[i]),"training_images")


# # file1=open('encodefile1.p','rb')
# # list_encode_id=pickle.load(file1)
# # l,ids = list_encode_id

# # print(l)
# # print(ids)