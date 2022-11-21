from PixCel import *

h=30
w=h*(25//10)

def isCollideX(cx,r):
	if (cx+r+1)>=w or (cx-(r+1))<=0:
		return True
	return False

def isCollideY(cy,r):
	if (cy+r+1)>=h or (cy-(r+1))<=0:
		return True
	return False

n=15
trailsX=[]
trailsY=[]
trailsSize=0

cx=10
cy=10
vx=2
vy=2
r=7

while(True):
	clearCanvas()

	for i in range(0,w):
		drawPoint(i,0)
	for i in range(0,w):
		drawPoint(i,h-1)
	for i in range(0,h):
		drawPoint(0,i)
	for i in range(0,h):
		drawPoint(w-1,i)

	trailsX.append(cx)
	trailsY.append(cy)
	trailsSize+=1

	if(len(trailsX)>n):
		trailsX.pop(0)
		trailsY.pop(0)
		trailsSize=n

	for i in range(0,trailsSize):
		currX=trailsX[i]
		currY=trailsY[i]
		drawPoint(currX,currY,'#')

	drawCircle(int(cx),int(cy),r)

	if isCollideX(cx,r):
		vx=vx*(-1)
	if isCollideY(cy,r):
		vy=vy*(-1)
	
	cx=cx+vx
	cy=cy+vy
	
	drawCanvas()


