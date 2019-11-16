
'''
*****************************************************************************************
*
*        		===============================================
*           		Rapid Rescuer (RR) Theme (eYRC 2019-20)
*        		===============================================
*
*  This script is to implement Task 1A of Rapid Rescuer (RR) Theme (eYRC 2019-20).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''


# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_1a.py
# Functions:		readImage, solveMaze
# 					[ Comma separated list of functions in this file ]
# Global variables:	CELL_SIZE
# 					[ List of global variables defined in this file ]


# Import necessary modules
# Do not import any other modules
import cv2
import numpy as np
import os


# To enhance the maze image
import image_enhancer


# Maze images in task_1a_images folder have cell size of 20 pixels
CELL_SIZE = 20


def readImage(img_file_path):

	"""
	Purpose:
	---
	the function takes file path of original image as argument and returns it's binary form

	Input Arguments:
	---
	`img_file_path` :		[ str ]
		file path of image

	Returns:
	---
	`original_binary_img` :	[ numpy array ]
		binary form of the original image at img_file_path

	Example call:
	---
	original_binary_img = readImage(img_file_path)

	"""

	binary_img = None

	#############	Add your Code here	###############

	img = cv2.imread(img_file_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, binary_img= cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
	
	#############	Print	###########################

	#print(ret)
	#print(img.shape, binary_img.shape)
	#cv2.imshow('binary', binary_img)
	#cv2.imshow('original', img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	###################################################

	return binary_img


def solveMaze(original_binary_img, initial_point, final_point, no_cells_height, no_cells_width):

	"""
	Purpose:
	---
	the function takes binary form of original image, start and end point coordinates and solves the maze
	to return the list of coordinates of shortest path from initial_point to final_point

	Input Arguments:
	---
	`original_binary_img` :	[ numpy array ]
		binary form of the original image at img_file_path
	`initial_point` :		[ tuple ]
		start point coordinates
	`final_point` :			[ tuple ]
		end point coordinates
	`no_cells_height` :		[ int ]
		number of cells in height of maze image
	`no_cells_width` :		[ int ]
		number of cells in width of maze image

	Returns:
	---
	`shortestPath` :		[ list ]
		list of coordinates of shortest path from initial_point to final_point

	Example call:
	---
	shortestPath = solveMaze(original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

	"""
	
	shortestPath = []

	#############	Add your Code here	###############

	## input parameter i get
	# original_binary_img
	# initial_point
	# final_point
	# no_cells_height
	# no_cells_width
	i_x, i_y = initial_point
	i, j = 0, 0

	## temprary maze image : which stores image of cell
	maze = np.zeros((CELL_SIZE, CELL_SIZE), dtype=int)
	h_m, w_m = maze.shape

	## ans is the matrix that will be solved 
	## with help of shortest path algorithms
	ans = np.zeros((2*no_cells_width, 2*no_cells_height), dtype=int)
	h_a, w_a = ans.shape

	height_binary, width_binary = original_binary_img.shape

	## IMPORTANTS 
	## 
	## while i reaches end
	##    |
	##    while j reaches end
	##    |   |
	##    |   check the cell image for right and bottom walls
	##    |   |
	##    |   if (walls)
	##    |   |   |
	##    |   |   mark corrosponding index in ans matrix as 1

	while(i < height_binary):
		while(j < width_binary):
			maze = original_binary_img[i:i + CELL_SIZE, j:j + CELL_SIZE]
			#print(i, j)

			#i / 10 because it was /20 then *2 
			ans[int(2*i/CELL_SIZE)][int(2*j/CELL_SIZE)] = 1#255

			## Diagnostic prints
			#print(maze[2][w-2])
			#print(maze[h-2][2])
			#plt.imshow(maze)
			#plt.show()


			## wall = 0
			## not wall = 255
			## The ifNotWall? logic
			if(int(maze[h_m//2][w_m-1]) == 255):
				ans[int(2*i/CELL_SIZE)][int(2*j/CELL_SIZE)+1] = 1#255
			if(int(maze[h_m-1][w_m//2]) == 255):
				ans[int(2*i/CELL_SIZE)+1][int(2*j/CELL_SIZE)] = 1#255
			if(i != 0 and int(maze[0][w_m//2] == 0)):
				ans[int(2*i/CELL_SIZE)-1][int(2*j/CELL_SIZE)] = 0#255
			if(j != 0 and int(maze[h_m//2][0] == 0)):
				ans[int(2*i/CELL_SIZE)][int(2*j/CELL_SIZE)-1] = 0#255
			#if(maze[5][5] == 0):
			#    ans[int(2*i/CELL_SIZE)][int(2*j/CELL_SIZE)+1] = 0
			#     ans[int(2*i/CELL_SIZE)+1][int(2*j/CELL_SIZE)] = 0


			#print(ans)

			j = j + CELL_SIZE
		j = 0
		i = i + CELL_SIZE

	#print('converted', ans.shape)
	#print(ans)

	answer = ans
	answer = np.delete(ans, h_a - 1, 0)
	answer = np.delete(answer, w_a - 1, 1)

	maze = answer.tolist()


	# Maze size 
	N = int(2*width_binary/CELL_SIZE-1)
	# Creating a 4 * 4 2-D list 
	sol = [ [ 0 for j in range(N) ] for i in range(N) ] 
	wasHere = np.zeros((2*no_cells_width - 1, 2*no_cells_height - 1), dtype=int)


	def printSolution( sol ): 

		for i in sol: 
			for j in i: 
				print(str(j) + " ", end ="") 
			print("")


	def isSafe( maze, x, y ): 

		if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
			return True

		return False

	def solveMaze2( maze ): 

		if solveMazeUtil(maze, 2*i_x, 2*i_y, sol) == False: 
			print("Solution doesn't exist What to do????")
			#printSolution( wasHere )
			return False

		#printSolution(sol) 
		return True

	def solveMazeUtil(maze, x, y, sol): 
		#print('\n', sol)
		# if (x, y is goal) return True 
		if x == N-1 and y == N-1: ####################################################################################
			sol[x][y] = 1
			return True

		# Check if maze[x][y] is valid 
		if isSafe(maze, x, y) == True: 
			# mark x, y as part of solution path 
			sol[x][y] = 1
			wasHere[x][y] = 1

			curr_x = N-1-x
			curr_y = N-1-y

			if(curr_x > curr_y):
					key = 1
			else:
					key = 2

			
			# Move forward in x direction
			if(key == 1): 
				key = 2
				if(x + 1 != N and wasHere[x + 1][y] != 1):	
					if solveMazeUtil(maze, x + 1, y, sol) == True: 
						return True
			# If moving in x direction doesn't give solution 
			# then Move down in y direction 
			if(key == 2):
				key = 1
				if(y + 1 != N and wasHere[x][y + 1] != 1):	
					if solveMazeUtil(maze, x, y + 1, sol) == True: 
						return True

			if(key == 1): 
				if(x + 1 != N and wasHere[x + 1][y] != 1):	
					if solveMazeUtil(maze, x + 1, y, sol) == True: 
						return True

			if(x != 0 and wasHere[x-1][y] != 1):
					if solveMazeUtil(maze, x - 1, y, sol) == True: 
						#sol[x][y] = 1
						#wasHere[x][y] = 1
						return True

			if(y != 0 and wasHere[x][y-1] != 1 ):
					if solveMazeUtil(maze, x, y-1, sol) == True: 
						#sol[x][y] = 1
						#wasHere[x][y] = 1
						return True
			
			# If none of the above movements work then 
			# BACKTRACK: unmark x, y as part of solution path 
			sol[x][y] = 0
			wasHere[x][y] = 1
			return False

	solveMaze2( maze )

	solution = []
	wasHere = np.zeros((2*no_cells_width - 1, 2*no_cells_height - 1), dtype=bool)

	def isSafe2(x, y): 
		if x >= 0 and x < N and y >= 0 and y < N and sol[x][y] == 1 and wasHere[x][y] == False: 
			wasHere[x][y] = True
			#print('yes:)', (x, y))
			return True
		#print('no:(')
		return False

	def final(x, y):
		if x == N-1 and y == N-1:
			solution.append((x, y))
			return True

		if(isSafe2(x, y) == True):
			solution.append((x, y))
			final(x + 1, y    )
			final(x    , y + 1)
			final(x - 1, y    )
			final(x    , y - 1)
		return False

	final(2*i_x, 2*i_y)

	i = 0
	#print(len(solution))

	while(i <= len(solution)):
		p, q = solution[i]
		p = int(p / 2)
		q = int(q / 2)
		shortestPath.append((p, q))
		i = i + 2
	#print(shortestPath)
	#print(len(shortestPath))
 
	###################################################
	
	return shortestPath


#############	You can add other helper functions here		#############



#########################################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:	main
# Inputs:			None
# Outputs: 			None
# Purpose: 			the function first takes 'maze00.jpg' as input and solves the maze by calling readImage
# 					and solveMaze functions, it then asks the user whether to repeat the same on all maze images
# 					present in 'task_1a_images' folder or not

if __name__ == '__main__':

	curr_dir_path = os.getcwd()
	img_dir_path = curr_dir_path + '/../task_1a_images/'				# path to directory of 'task_1a_images'
	
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'		# path to 'maze00.jpg' image file

	print('\n============================================')

	print('\nFor maze0' + str(file_num) + '.jpg')

	try:
		
		original_binary_img = readImage(img_file_path)
		height, width = original_binary_img.shape

	except AttributeError as attr_error:
		
		print('\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
		exit()
	
	no_cells_height = int(height/CELL_SIZE)							# number of cells in height of maze image
	no_cells_width = int(width/CELL_SIZE)							# number of cells in width of maze image
	initial_point = (0, 0)											# start point coordinates of maze
	final_point = ((no_cells_height-1),(no_cells_width-1))			# end point coordinates of maze

	try:

		shortestPath = solveMaze(original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

		if len(shortestPath) > 2:

			img = image_enhancer.highlightPath(original_binary_img, initial_point, final_point, shortestPath)
			
		else:

			print('\n[ERROR] shortestPath returned by solveMaze function is not complete !\n')
			exit()
	
	except TypeError as type_err:
		
		print('\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
		exit()

	print('\nShortest Path = %s \n\nLength of Path = %d' % (shortestPath, len(shortestPath)))
	
	print('\n============================================')
	
	cv2.imshow('canvas0' + str(file_num), img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	choice = input('\nWant to run your script on all maze images ? ==>> "y" or "n": ')

	if choice == 'y':

		file_count = len(os.listdir(img_dir_path))

		for file_num in range(file_count):

			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			print('\n============================================')

			print('\nFor maze0' + str(file_num) + '.jpg')

			try:
				
				original_binary_img = readImage(img_file_path)
				height, width = original_binary_img.shape

			except AttributeError as attr_error:
				
				print('\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
				exit()
			
			no_cells_height = int(height/CELL_SIZE)							# number of cells in height of maze image
			no_cells_width = int(width/CELL_SIZE)							# number of cells in width of maze image
			initial_point = (0, 0)											# start point coordinates of maze
			final_point = ((no_cells_height-1),(no_cells_width-1))			# end point coordinates of maze

			try:

				shortestPath = solveMaze(original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

				if len(shortestPath) > 2:

					img = image_enhancer.highlightPath(original_binary_img, initial_point, final_point, shortestPath)
					
				else:

					print('\n[ERROR] shortestPath returned by solveMaze function is not complete !\n')
					exit()
			
			except TypeError as type_err:
				
				print('\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
				exit()

			print('\nShortest Path = %s \n\nLength of Path = %d' % (shortestPath, len(shortestPath)))
			
			print('\n============================================')

			cv2.imshow('canvas0' + str(file_num), img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
	
	else:

		print('')


