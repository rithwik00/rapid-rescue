
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


