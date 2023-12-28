from utils import auto_run
import cv2

def main(video_name:str="video/polaris.mov"):
    print("Hello")
    cap = cv2.VideoCapture(video_name)

    while True:
        ret, frame = cap.read()

        if ret:
            re_f = cv2.resize(frame,(int(len(frame[0]) / 4),int(len(frame) / 4)))
            g_f = cv2.cvtColor(re_f,cv2.COLOR_BGR2GRAY)
            _, g_f = cv2.threshold(g_f,200,255,type=cv2.THRESH_BINARY)
            cv2.imshow("test",g_f)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    cv2.destroyWindow("test")
if __name__=="__main__":
    auto_run(main)