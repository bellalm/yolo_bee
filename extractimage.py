# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:14:24 2022

@author: bella
"""

import cv2
import pandas as pd
from random import randrange
import numpy as np
  
  
File_data = np.loadtxt(r"C:\Users\bella\Documents\stage_pfe\yoloultra\yolov5\runs\detect\exp58\000000.txt")
img = cv2.imread(r'C:\Users\bella\Documents\stage_pfe\yoloultra\yolov5\data\000000.png')


df = pd.DataFrame(File_data)

h,w,d= img.shape
df[1]=df[1]*w
df[2]=df[2]*h
df[3]=df[3]*w
df[4]=df[4]*h

df["t_x"]=df[1]-df[3]/2
df["t_y"]=df[2]-df[4]/2
df["b_x"]=df[1]+df[3]/2
df["b_y"]=df[2]+df[4]/2

df["t_x"]=df["t_x"].astype(int)
df["t_y"]=df["t_y"].astype(int)
df["b_x"]=df["b_x"].astype(int)
df["b_y"]=df["b_y"].astype(int)

n=0

image = img[ df["t_y"][n]:df["b_y"][n],df["t_x"][n]:df["b_x"][n]]
test = cv2.imwrite(r"D:\videos\videos\{0:06d}.png".format(n), image)  


n=1
for index, row  in df.iterrows():
    randomT_X=randrange(3,12)
    randomT_Y=randrange(3,12)
    randomB_X=randrange(3,12)
    randomB_Y=randrange(3,12)
    image = img[ int(row['t_y']-randomT_Y):int(row['b_y']+randomB_Y),int(row['t_x']-randomT_X):int(row['b_x']+randomB_X)]
    print(n)
    n+=1
    try:
        test = cv2.imwrite(r"D:\videos\videos\{0:06d}.png".format(n), image)  
    except:    
        image = img[ int(row['t_y']):int(row['b_y']),int(row['t_x']):int(row['b_x'])]
        test = cv2.imwrite(r"D:\videos\videos\{0:06d}.png".format(n), image) 
        print("eror")
        
    