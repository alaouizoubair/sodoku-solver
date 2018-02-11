#!/usr/bin/python

from copy import copy, deepcopy

class Sodoku:
	'Sodoku class'	
	h=9
	w=9
	#This function initializes the class
	def __init__(self):
		self.x=0
		self.y=0
		self.v=0
		self.T=[[0 for i in range(Sodoku.h)]for j in range(Sodoku.w)]
		self.initTable()
		print 'Table initiated'

	#I hard coded some values in the table so I can test my solving algorithm
	def initTable(self):
		self.T[0][2]=6
		self.T[0][5]=8
		self.T[0][6]=5
		self.T[1][4]=7
		self.T[1][6]=6
		self.T[1][7]=1
		self.T[1][8]=3
		self.T[2][8]=9
		self.T[3][4]=9
		self.T[3][8]=1
		self.T[4][2]=1
		self.T[4][6]=8
		self.T[5][0]=4
		self.T[5][3]=5
		self.T[5][4]=3
		self.T[6][0]=1
		self.T[6][2]=7
		self.T[6][4]=5
		self.T[6][5]=3
		self.T[7][1]=5
		self.T[7][4]=6
		self.T[7][5]=4
		self.T[8][0]=3
		self.T[8][3]=1
		self.T[8][7]=6

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
		elif self.checkLine(x-1)==0:
			print "Oups!! Value already in line"
			self.T[x-1][y-1]=0
		elif self.checkColumn(y-1)==0:
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
	def checkLine(self,x):
		values = []
		for i in range(Sodoku.w):
			if self.T[x][i] != 0:
				values.append(self.T[x][i])

		for i in values:
			if values.count(i)>1:
				return 0

		return 1
	#Confusion happened between row and colomn
	def checkColumn(self,y):
		values = []
		for i in range(Sodoku.h):
			if self.T[i][y] != 0:
				values.append(self.T[i][y])

		for i in values:
			if values.count(i)>1:
				return 0

		return 1


	def displayTable2(self,T2):
		for i in range(self.h):
			if i == 0:
				print "    1 2 3   4 5 6   7 8 9  "
				print "  + - - - + - - - + - - - +"

			for j in range(self.w):
				if j == 0:
					print i+1 ,

				if j == 0 or j == 3 or j == 6:
					print "|",
				if T2[i][j] == 0:
					print ".",
				else:
					print T2[i][j],
			print "|"

			if i == 2 or i == 5 or i == 8:
				print "  + - - - + - - - + - - - +" 

	def checkSquare2(self,T2,x,y):
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
				if T2[i][j]!=0:
					values.append(T2[i][j])

		for i in values:
			if(values.count(i)>1):
				return 0

		return 1

	def checkLine2(self,T2,x):
		values = []
		for i in range(Sodoku.w):
			if T2[x][i] != 0:
				values.append(T2[x][i])

		for i in values:
			if values.count(i)>1:
				return 0

		return 1
	
	def checkColumn2(self,T2,y):
		values = []
		for i in range(Sodoku.h):
			if T2[i][y] != 0:
				values.append(T2[i][y])

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


	def findPossibilities(self,x,y):
		T2 = deepcopy(self.T)
		listp = []

		if T2[x][y] != 0:
			return listp

		for v in range(1,10):
			T2[x][y] = v
			if self.checkColumn2(T2,y) and self.checkLine2(T2,x) and self.checkSquare2(T2,x,y):
				listp.append(v)

		return listp

	def fillSodoku(self):
		cond = 0
		for x in range(9):
			for y in range(9):
				listp = self.findPossibilities(x,y)
				print x+1 , y+1 , listp
				if len(listp) == 1:
					self.T[x][y] = listp[0]
					self.displayTable()
					cond = 1
		print "ok"
		return cond

	def fillSodoku2(self):
		for x in range(9):
			for y in range(9):
				if self.T[x][y] == 0:
					listp = self.findPossibilities(x,y)
					if len(listp) == 0:
						return 0
					else:
						for v in listp:
							print x+1, y+1 ,listp
							self.T[x][y] = v
							self.displayTable()
							# a = raw_input("")
							if self.fillSodoku2()==1:
								return 1
							else:
								self.T[x][y] = 0

						return 0
		return 1


	def solveSodoku(self):
		cpt=0

		while self.fillSodoku():
			cpt=cpt+1
			if cpt > 1000:
				return 0

		return 1


