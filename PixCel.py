import xlwings as xw

h=70
w=120

def init():
	
	global wb
	global sht1
	global Matrix

	wb = xw.Book('Canvas.xlsx')
	sht1 = wb.sheets['Sheet1']
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
	wb.save('Canvas.xlsx')

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
