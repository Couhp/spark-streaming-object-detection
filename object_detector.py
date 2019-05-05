
from threading import Thread
from imageai.Detection import ObjectDetection
import cv2
import os

# detector 
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("coco.h5")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="exam.png",
                                             output_image_path="result.png",
                                             minimum_percentage_probability=30)


class ObjectDetect(Thread):
    def __init__(self, data, output_path):
        Thread.__init__(self)
        self.data = data
        self.output_path = output_path

    def run(self):
        detections = detector.detectObjectsFromImage(input_type='array',
                                                     input_image=self.data,
                                                     output_image_path=self.output_path,
                                                     minimum_percentage_probability=30)



