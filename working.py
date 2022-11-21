import xlwings as xw

wb = xw.Book('Canvas.xlsx')
sht1 = wb.sheets['Sheet1']

h=30
w=h*(25//10)

Matrix = [['_' for x in range(w)] for y in range(h)]

sht1.autofit()
sht1.clear_contents()

def drawPoint(x,y,c='#'):
	Matrix[y][x]=c 


def drawCanvas():
	for i in range(0,h):
		fillchar=""
		for j in range(0,w):
			fillchar+=Matrix[i][j]+"  "
		sht1.range('A'+str(i+1)).value=fillchar

def clearCanvas():
	for i in range(0,h):
		for j in range(0,w):
			Matrix[i][j]='_'

def drawCircle(cx,cy,r,c='#'):
	bx=cx-r
	by=cy-r

	ex=cx+r
	ey=cy+r

	for yn in range(by,ey+1):
		for xn in range(bx,ex+1):
			dx=cx-xn
			dy=cy-yn
			if((dx*dx) + (dy*dy) <= r*r):
				drawPoint(xn,yn,c)



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

	wb.save('Canvas.xlsx')
