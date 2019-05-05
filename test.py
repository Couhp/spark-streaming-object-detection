import cv2
import lightnet
import numpy as np
import time

import lightnet

model = lightnet.load('tiny-yolo')


image = lightnet.Image.from_bytes(open('eagle.jpg', 'rb').read())
boxes = model(image)