"""
Author: Madeline Seifert
Date Created: 8/14/2023

This is a recreation of the mobile game Tens! by Kwalee.
The goal of this game is to place dice on the board so that the total value
of a row/column adds up to exactly ten. 
"""

import random as rand

displays = "□⚀⚁⚂⚃⚄⚅"


class Dice:

	"""Create a dice"""
	def __init__(self, value = 0):
		if value == 0: #if no value entered, aka Dice()
			self.value == 0
		else:
			self.value = value
			self.display = displays[self.value]


class DiceBoard:
	board = []

	"""Constructs an empty board"""
	def __init__(self):
		for i in range(0,5):
			self.board.append([]) #add an array for each row
			for j in range(0,5):
				self.board[i].append(None) #add a placeholder so we know this square of the board is empty


	"""Returns the total value of all the dice in one column, col"""
	def getColTotal(self, col):
		colTotal = 0
		
		for i in range(0,5):
			if self.board[i][col] != None:
				colTotal += self.board[i][col].value #pulls value of one dice in the column & adds to total only if there is a dice object here
		return colTotal

	"""Returns the total value of all the dice in one row"""
	def getRowTotal(self, row):
		rowTotal = 0

		for j in range(0,5):
			if self.board[row][j] != None:
				rowTotal += self.board[row][j].value #pulls value of one dice in row & adds to total only if there is a dice object here
		return rowTotal

	"""Adds a dice to the board"""
	def addDice(self, row, col, dice):
		self.board[row][col] = dice

	"""Removes a dice from the board"""
	def removeDice(self, row, col):
		return row
	
	
	"""Prints the board, along with the totals of each row and column"""
	def print(self):
		bStr = ""

		#add column totals above the board
		for i in range(0,5):
			bStr += str(self.getColTotal(i))
			bStr += " "
		bStr += "\n"
		for i in range(0,5):
			for j in range(0,5):
				if self.board[i][j] != None: #if there's a dice
					bStr += self.board[i][j].display + " "
				else:
					bStr += "□ "
			bStr += str(self.getRowTotal(i))
			bStr += "\n"
			
		print(bStr)
	


#Testing
dboard = DiceBoard()
dboard.print()

dboard.addDice(1,2,Dice(2))
dboard.print()

