
# coding: utf-8

# In[ ]:


import face_recognition
import os
import matplotlib.pyplot as plt
import time
get_ipython().magic('matplotlib inline')


# In[ ]:


def or_list(list1,list2):
    sum_list = [a + b for a, b in zip(list1, list2)]
    return sum_list


# In[ ]:


#Load known faces
names = []
known_faces = []
length = 0
for image in os.listdir('known_faces/'):
    known = face_recognition.load_image_file("known_faces/" + image)
    known_encoding = face_recognition.face_encodings(known)[0]
    known_faces.append(known_encoding)
    names.append(image.split('.')[0])
    length += 1


# In[ ]:


#Check which known faces are there in the unknown image
result = [False]*length
img_test = 'barack.jpg'
unknown_picture = face_recognition.load_image_file("unknown_faces/" + img_test)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
for unknown_face in unknown_face_encoding:
    result_temp = face_recognition.compare_faces(known_faces, unknown_face)
    result = or_list(result,result_temp)


# In[ ]:


#print results which are True
present = False
plt.imshow(unknown_picture)
print('Known people present in the photo are :')
for i in range(result.__len__()):
    if result[i] == True:
        present = True
        print('Present {}'.format(names[i]))
if present==False:
    print('No known face found')

