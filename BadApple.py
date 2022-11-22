import numpy as np
import cv2

from PixCel import *

vidcap = cv2.VideoCapture("BadApple.mp4")

success, image = vidcap.read()


i=0
init()

while success:
	clearCanvas()
	
	success, image = vidcap.read()

	resize = cv2.resize(image, (60, 60))

	if i%2:
		for idx, x in np.ndenumerate(resize):
			if x==0:
				drawPoint(idx[1],idx[0])
		drawCanvas()

	if cv2.waitKey(10) == 27:
		break
	i+=1
