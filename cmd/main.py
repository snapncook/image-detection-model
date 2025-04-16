import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import yaml
from io import BytesIO
from PIL import Image

import grpc
from concurrent import futures

import detection_pb2 as proto
import detection_pb2_grpc as proto_grpc

import logging
from ultralytics import YOLO

def save_bytes_as_image(image_bytes, file_path):
    image_stream = BytesIO(image_bytes)
    image = Image.open(image_stream)
    image = image.convert('RGB')
    image.save(file_path)

class YOLODetectionService(proto_grpc.DetectionService):
    def __init__(self):
        logging.info("Initializing DetectionService...")
        try:
            self.model = YOLO(cfg["best"])
            logging.info("Model loaded successfully from: %s", cfg["best"])
        except Exception as e:
            logging.error("Error loading model: %s", str(e))
            raise

    def detect(self, image_path):
        logging.info("Running detection on image: %s", image_path)
        try:
            results = self.model(image_path, conf=cfg["conf"])
            logging.info("Detection complete. Parsing results...")

            detected_classes = results[0].names  
            class_ids = results[0].boxes.cls.tolist() 
            class_names = [detected_classes[int(cls_id)] for cls_id in class_ids]

            unique_class_names = list(set(class_names))
            logging.info("Detected objects: %s", unique_class_names)
            return unique_class_names
        except Exception as e:
            logging.error("Detection failed: %s", str(e))
            return []
    
    def YOLODetect(self, request, context):
        path = 'image.jpg' 
        image = request.image
        save_bytes_as_image(image, path)
        
        objs = self.detect(path)
        return proto.YOLODetectionResponse(objects=objs)

def main():
    service = YOLODetectionService()
    port = cfg["port"]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_grpc.add_DetectionServiceServicer_to_server(service, server)
    server.add_insecure_port("[::]:" + port)
    server.start()

    logging.info("gRPC server started on port " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    with open('configs/config.yml') as f:
        cfg = yaml.safe_load(f)
    
    main()