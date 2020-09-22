import pandas as pd
import cv2


def design(name,index):
	image = cv2.imread('pic.jpg',cv2.IMREAD_UNCHANGED)
	position = (1300,1240)
	cv2.putText(image,name,position,cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0,0),5)
	cv2.imwrite('cert/'+str(i)+"_"+name+".jpg",image)

data = pd.read_csv("list.csv")
size = len(data)
i = 0
while(i < size):
	name = data.iloc[i][0]
	design(name,i)
	i = i + 1