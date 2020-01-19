'''
鱼塘杀鱼事件
'''

import time
import os
import random

class Fish:
	pos_x = 0
	pos_y = 0
	
	def __init__(self, x, y):
		self.pos_x = x
		self.pos_y = y
	def move(self, offset_x, offset_y):
		self.pos_x += offset_x
		self.pos_y += offset_y
		
		
class Shark(Fish):
	pass
	
	

class Fishpond:
	fishes = []
	sharkes = []
	pond_info = []
	_length = 10
	_width = 10
	
	def __init__(self, length = 10, width = 10):
		self._length = length
		self._width = width
		for x in range(0, self._length):
			row = []
			for y in range(0, self._width):
				row.append(0)
			self.pond_info.append(row)
		
	def addFishes(self, x, y):
		f = Fish(x, y)
		self.fishes.append(f)
		(self.pond_info[x])[y] = 1
		
	def addSharkes(self, x, y):
		S = Shark(x, y)
		self.sharkes.append(S)
		(self.pond_info[x])[y] = 2

	def show(self):
		for row in self.pond_info:
			str_show = ''
			for point in row:
				if point == 0:
					str_show += '  .  '
				elif point == 1:
					str_show += '  *  '
				elif point == 2:
					str_show += ' <-> '
			print(str_show, '\n')
			
	def fishes_move(self, x, y):
		for fish in self.fishes:
			if (fish.pos_x + x < self._length and 
				fish.pos_x + x >= 0 and
				fish.pos_y + y < self._width and
				fish.pos_y + y >= 0 and
				(self.pond_info[fish.pos_x + x])[fish.pos_y + y] == 0):
					(self.pond_info[fish.pos_x])[fish.pos_y] = 0
					fish.move(x, y)
					(self.pond_info[fish.pos_x])[fish.pos_y] = 1
					
	def sharkes_move(self, x, y):		
		for shark in self.sharkes:
			if (shark.pos_x + x < self._length and 
				shark.pos_x + x >= 0 and
				shark.pos_y + y < self._width and
				shark.pos_y + y >= 0 and
				(self.pond_info[shark.pos_x + x])[shark.pos_y + y] != 2):
					if self.pond_info[shark.pos_x + x][shark.pos_y + y] == 1:
						for fish in self.fishes:	
							if((shark.pos_x + x) == fish.pos_x and
								(shark.pos_y + y) == fish.pos_y):
									self.fishes.remove(fish)
									del fish
									break
									
					(self.pond_info[shark.pos_x])[shark.pos_y] = 0
					shark.move(x, y)
					(self.pond_info[shark.pos_x])[shark.pos_y] = 2


fp = Fishpond(6, 6)
fp.addFishes(1, 1)
fp.addFishes(1, 2)
fp.addFishes(1, 3)
fp.addFishes(1, 4)
fp.addFishes(1, 5)

fp.addSharkes(2,5)

game_end = False

while game_end != True:
	fp.show()
	time.sleep(1)
	os.system("cls")
	
	x = random.randint(-1,1)
	y = random.randint(-1,1)
	fp.fishes_move(x, y)
	
	x = random.randint(-1,1)
	y = random.randint(-1,1)
	fp.sharkes_move(x, y)
	
	if(len(fp.fishes) == 0):
		game_end = True
	
		
		
		
