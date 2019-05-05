import socket, pickle
import cv2
import numpy as np
import codecs

host = 'localhost'
port = 9999


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)

frames = ""

def resize(frame):
    height , width , layers =  frame.shape
    new_h = 300   
    new_w= int(np.floor(300 * width / height))
    resize_frame = cv2.resize(frame, (new_w, new_h)) 
    return resize_frame

def send(content):
    conn, addr = s.accept()
    conn.send(content)
    conn.close()

cap = cv2.VideoCapture('video.mp4')
counter = 0
frames = []
    
while(cap.isOpened()):
    counter += 1
    if counter % 8 != 0:
        continue
    
    ret, frame = cap.read()
    
    if ret==True:
        frame = resize(frame)
    
        content_base64 = codecs.encode(pickle.dumps(frame), "base64")\
                                .decode()\
                                .replace("\n", "#newline#") # string 
        # content = codecs.encode(content_base64, "utf-8")
        frames.append(content_base64)
    else:
        break

    if len(frames) == 6:
        content = codecs.encode('\n'.join(frames), "utf-8")
        send(content)
        frames = []

s.close()

