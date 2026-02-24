import cv2
from ultralytics import YOLO
import sys

MODEL_PATH = '../models/best.pt'

def run_inference(image_path):
    try:
        
        model = YOLO(MODEL_PATH)
        
        results = model.predict(image_path, imgsz=1024, conf=0.45, save=True)
       
        for result in results:
            result.show() 
            
            print(f"✅ Tespit Tamamlandı! {len(result.boxes)} yaprak bulundu.")
            
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
        run_inference(img_path)
    else:

        print("Kullanım: python inference.py <resim_yolu>")
