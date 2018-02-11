#!/usr/bin/python

class Sodoku:
	'Sodoku class'	
	h=9
	w=9
	def __init__(self):
		self.x=0
		self.y=0
		self.v=0
		self.T=[[0 for i in range(Sodoku.w)]for j in range(Sodoku.h)]
		# self.T = [][]
		print 'Table initiated'

	def displayTable(self):
		for i in range(self.h):
			if i == 0:
				print "    1 2 3   4 5 6   7 8 9  "
				print "  + - - - + - - - + - - - +"

			for j in range(self.w):
				if j == 0:
					print i+1 ,

				if j == 0 or j == 3 or j == 6:
					print "|",
				if self.T[i][j] == 0:
					print ".",
				else:
					print self.T[i][j],
			print "|"

			if i == 2 or i == 5 or i == 8:
				print "  + - - - + - - - + - - - +" 

	def insertValue(self):
		done = 0
		while not done:
			done = 1
			try:
				x = raw_input('Choose row: ')
				if not x :
					print "Please choose a row"
					return
				x = int(x)
				y = raw_input('Choose colomn: ')
				if not x :
					print "Please choose a row"
					return
				y = int(y)
				v = raw_input('Choose value between 1 and 9: ')
				if not x :
					print "Please choose a row"
					return
				v = int(v)
				if x<1 or x>9 or y<1 or y>9 or v<1 or v>9:
					print "Values incorrect"
					done = 0 
			except ValueError:
				done = 0
				print ('Entered value not valid. Please try again')

	

		self.T[x-1][y-1]=v
		if self.checkSquare(x-1,y-1) == 0:
			print "Oups!! Value already in square"
			self.T[x-1][y-1]=0
		elif self.checkLine(y-1)==0:
			print "Oups!! Value already in line"
			self.T[x-1][y-1]=0
		elif self.checkColumn(x-1)==0:
			print "Oups!! Value already in column"
			self.T[x-1][y-1]=0



	def checkSquare(self,x,y):
		if x<3 :
			x=0
		elif x<6:
			x=3
		else:
			x=6

		if y<3 :
			y=0
		elif y<6:
			y=3
		else:
			y=6

		values = []

		for i in range(x,x+3):
			for j in range(y,y+3):
				if self.T[i][j]!=0:
					values.append(self.T[i][j])

		for i in values:
			if(values.count(i)>1):
				return 0

		return 1

	#Confusion happened between row and colomn
	def checkLine(self,y):
		values = []
		for i in range(Sodoku.w):
			if self.T[i][y] != 0:
				values.append(self.T[i][y])

		for i in values:
			if values.count(i)>1:
				return 0

		return 1
	#Confusion happened between row and colomn
	def checkColumn(self,x):
		values = []
		for i in range(Sodoku.h):
			if self.T[x][i] != 0:
				values.append(self.T[x][i])

		for i in values:
			if values.count(i)>1:
				return 0

		return 1

	def gameEnded(self):
		for i in self.T:
			if i.count(0) != 0:
				return 0

		for i in range(Sodoku.w):
			for j in range(Sodoku.h):
				if self.checkColumn(i,j)==0 or self.checkLine(i,j)==0 :
					return 0



		for x in range(0,Sodoku.w,3):
			for y in range(0,Sodoku.h,3):
				if self.checkSquare(x,y) == 0:
					return 0

		return 1


	def playGame(self):
		while not self.gameEnded():
			self.displayTable()
			self.insertValue()

		print "YOU WIN"	

