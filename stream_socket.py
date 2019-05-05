import socket, pickle
import cv2
import numpy as np
import codecs

host = 'localhost'
port = 9999


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)



def resize(frame):
    height , width , layers =  frame.shape
    new_h = 300   
    new_w= int(np.floor(300 * width / height))
    resize_frame = cv2.resize(frame, (new_w, new_h)) 
    return resize_frame



cap = cv2.VideoCapture('video.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        conn, addr = s.accept()
        frame = resize(frame)
        
        content_base64 = codecs.encode(pickle.dumps(frame), "base64")\
                               .decode()\
                               .replace("\n", "#newline#") # string 
        content = codecs.encode(content_base64, "utf-8")
        conn.send(content)
        conn.close()
    else:
        break

s.close()

