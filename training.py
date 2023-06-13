from imutils import face_utils
from imutils.video import VideoStream
import time
import os
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import numpy as np
from sklearn.manifold import TSNE
import cv2



def train_images(directory):
    # Mở file để ghi quá trình train
    with open("train_log.txt", "w") as log_file:
        # Lặp qua tất cả các tệp trong thư mục
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(directory, filename)
                image = cv2.imread(image_path)

                # Tiến hành train dữ liệu
                # Viết quá trình train vào file log
                log_file.write(f"Hình ảnh đào tạo: {filename}\n")
                # Thêm các bước train dữ liệu ở đây

                log_file.write(f"Đào tạo hoàn thành cho hình ảnh: {filename}\n\n")

    print("Quá trình đào tạo hoàn thành.")

# Đường dẫn đến thư mục chứa các hình ảnh
directory = "face_user"
train_images(directory)




# def train():
#     training_dir='face_recognition_data/training_dataset'
#     count=0
#     for person_name in os.listdir(training_dir):
#         curr_directory=os.path.join(training_dir,person_name)
#         if not os.path.isdir(curr_directory):
#             continue 
#         for imagefile in image_files_in_folder(curr_directory):
#             count+=1         
#         X=[] 
#         y=[]
#         i=0
#         for person_name in os.listdir(training_dir):
#             print(str(person_name)) 
#             curr_directory=os.path.join(training_dir,person_name)
#             if not os.path.isdir(curr_directory):
#                 continue
#             for imagefile in image_files_in_folder(curr_directory): 
#                 print(str(imagefile)) 
#                 image=cv2.imread(imagefile) 
#                 try:
#                     X.append((face_recognition.face_encodings(image)[0]).tolist())
#                     y.append(person_name)
#                     i+=1  
#                 except:
#                     print("Loại Bỏ")
#                     os.remove(imagefile)
#             targets=np.array(y) 
#             encoder = LabelEncoder()
#             encoder.fit(y)  
#             y=encoder.transform(y)
#             X1=np.array(X) 
#             print("shape: "+ str(X1.shape)) 
#             np.save('face_recognition_data/classes.npy', encoder.classes_)
#             svc = SVC(kernel='linear',probability=True)
#             svc.fit(X1,y) 
#             svc_save_path="face_recognition_data/svc.sav" 
#             with open(svc_save_path, "w+b") as f: 
#                 pickle.dump(svc,f)

# if __name__ == "__main__":
# 	train()