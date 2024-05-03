from utils import auto_run
import cv2
from convert_ground import create_ground_grid

def main(video_name:str,width:int=1024,):
    cap = cv2.VideoCapture(video_name)
    
    xx, yy, valid_area = create_ground_grid

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow("test",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    cv2.destroyWindow("test")
    
if __name__=="__main__":
    auto_run(main)