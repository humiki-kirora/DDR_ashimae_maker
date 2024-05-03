import sys
import os
sys.path.append(os.path.curdir)
sys.path.append(os.path.pardir)

from utils import auto_run
import cv2

def main(video_name:str="video/polaris.mov",output_path:str="images"):
    cap = cv2.VideoCapture(video_name)
    
    os.makedirs("dump",exist_ok=True)
    os.makedirs(os.path.join("dump",output_path),exist_ok=True)
    
    i = 0
    while True:
        ret, frame = cap.read()
        i += 1

        if ret:
            cv2.imwrite(os.path.join("dump",output_path,f"{i}.jpg"),frame)
            cv2.imshow("test",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    cv2.destroyWindow("test")
if __name__=="__main__":
    auto_run(main)