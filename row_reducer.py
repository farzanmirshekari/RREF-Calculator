def take_input():
	rows = int(input("Enter the number of rows in the matrix: "))
	table = []
	for i in range(rows):
		print("Enter the values for row " + str(i + 1) + ":")
		val = input()
		table.append([int(x) for x in val.split()])
	if not all([len(row) == len(table[0]) for row in table]):
		print("INVALID ROW LENGTH, TRY AGAIN!")
		return take_input()
	return table

def calculate_rref(matrix, index = 0):
	if index == len(matrix):
		return matrix
	diagonal_val = matrix[index][index]
	if int(diagonal_val) != 0:
		for column in range(len(matrix[index])):
			matrix[index][column] /= diagonal_val
		this_row = matrix[index]
		for row in range(len(matrix)):
			if row != index:	
				multiply_factor = matrix[row][index]
				for column in range(len(matrix[row])):
					matrix[row][column] -= multiply_factor * this_row[column]
	return calculate_rref(matrix, index + 1)

def print_matrix(matrix):
	for row in range(len(matrix)):
		print(matrix[row])

def regulate_matrix(matrix):
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if(matrix[row][col] == -0.0):
				matrix[row][col] = 0.0
	return matrix
		

action = ""

while action != "NO":
	matrix = print_matrix(regulate_matrix(calculate_rref(take_input())))
	action = input("Do you wish to continute? (Yes / No): ").upper()