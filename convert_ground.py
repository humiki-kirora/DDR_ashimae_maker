import cv2
from utils import auto_run
from typing import List
import numpy as np
from scipy.spatial.transform  import Rotation

def create_rotation_matrix_from_depression_angle(depression_angle:float):
    R = Rotation.from_euler('x', -np.pi/2 * ((90 - depression_angle) / 90)).as_matrix()
    return R
    

def create_ground_grid(width, height, R, params,
                       dist:float = 1.0,radius:float = 3.0):
    fx = dist * width / (2 * radius)
    fy = dist * height / (2 * radius)
    cx = width / 2
    cy = height / 2
    
    x = np.linspace(0,width,width)
    y = np.linspace(0,height,height)
    x, y = np.meshgrid(x,y)
    
    X = (x - cx) / fx
    Y = (y - cy) / fy
    Z = 1
    
    X_ = R[0,0] * X + R[0,1] * Y + R[0,2] * Z  
    Y_ = R[1,0] * X + R[1,1] * Y + R[1,2] * Z 
    Z_ = R[2,0] * X + R[2,1] * Z + R[2,2] * Z
    
    x_ = X_ / Z_
    y_ = Y_ / Z_

    valid_area = (Z_ > 0)[...,None].astype(np.uint8)
    
    xx = fx * x_ + cx
    yy = fy * y_ + cy
    
    return xx, yy, valid_area
    
def main(image_path:str, width:int=1024, 
         height:int=1024, depression_angle:float=0, dist:float=1.0, radius:float=10.0):
    
    # imgae read
    image = cv2.imread(image_path)
    
    width = image.shape[1]
    height = image.shape[0]
    
    # create_grid
    R = create_rotation_matrix_from_depression_angle(depression_angle)
    xx,yy,valid = create_ground_grid(width,height,R,dist,radius)
    
    remapped = cv2.remap(image,xx.astype(np.float32),yy.astype(np.float32),cv2.INTER_CUBIC)
    remapped = remapped * valid
    
    cv2.imshow("iamge",image)
    cv2.imshow("test",remapped)
    cv2.waitKey(0)
        

if __name__=="__main__":
    auto_run(main)