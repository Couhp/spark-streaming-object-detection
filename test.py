from imageai.Detection import ObjectDetection
import os
import cv2
import pickle
from os.path import join
import io
import numpy as np
from PIL import Image
import codecs
import time
import shutil


detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(os.path.dirname(__file__), "yolo-tiny.h5"))
detector.loadModel()
detector.detectObjectsFromImage(input_image="exam.png",
                                output_image_path="result/exam.png",
                                minimum_percentage_probability=30) 