"""
File: boggle.py
Name: Ryan Lei
----------------------------------------
This is a boggle game.
User can input four letters in four rows.
After all letter imported, the program will start.
It will find all the anagrams for the letter next to it.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# Global variable
Word_Dict_Lst = []  # This empty list to store all dictionary word.


def main():
	"""
	This is a boggle game.
	User can input four letters in four rows.
	After all letter imported, the program will start.
	It will find all the anagrams for the letter next to it.
	"""
	read_dictionary()  # Call the dictionary.

	input_rows = []  # All letter that user inputted

	# Loop 4 times to let user input the letters.
	for i in range(4):

		# What user input should be case in sensitive, and split by space.
		letter_row = input(str(i + 1) + ' row of letters: ').lower().split()

		# When user input less than or more than 4 letter, print illegal put.
		if len(letter_row) == 0 or len(letter_row) != 4:
			print('illegal input')
			return False

		# When the letter is longer than 1, print illegal input.
		for letter in letter_row:
			if len(letter) > 1 or letter.isdigit():
				print('illegal input')
				return False

		# Add the letter to row.
		input_rows.append(letter_row)

	# When user input the wrong form, break the function.
	if input_rows is not False:

		# Empty list to store all the word in different anagram.
		current_lst = []

		# Build the neighbor letter board.
		board = []

		# Loop over the board to find the neighbor word.
		# Discuss with TA Gibbs on 2021/3/22.
		for y in range(len(input_rows)):
			for x in range(len(input_rows)):

				# Get different position of the board.
				board.append((x, y))

				# Get the letter in position that user input.
				current = input_rows[x][y]

				# Search the word in different anagram.
				search(input_rows, board, current, current_lst, x, y)
				board.pop()

		# Print the number of the matched word that matched in the dictionary.
		print('There are '+str(len(current_lst))+' words in total.')


def search(i_r, board, current, current_lst, x, y):
	"""
	This function is to find all the anagram letter that user input.
	:param i_r: list. To store the index of the anagram word.
	:param board: list. Build the neighbor of letter row.
	:param current: string. To store the current word in different anagram.
	:param current_lst: list. Word ready to add in All_Current word.
	:param x: int, the next original point of x for recursion.
	:param y: int, the next original point of x for recursion.
	"""
	# Discuss with TA Gibbs, Henry and Dennis on 2021/3/26.
	# Loop over the board. When the for loop end, base case.
	for i in range(-1, 2):
		for j in range(-1, 2):

			# When back to the original point, do nothing.
			if i == 0 and j == 0:
				pass
			else:

				# Get the next point of x, y
				next_x = x + i
				next_y = y + j

				# When next_x and next_y is in the board range
				if 0 <= next_x <= 3 and 0 <= next_y <= 3:
					# Position next_x and next_y not in board, add.
					if (next_x, next_y) not in board:
						board.append((next_x, next_y))

						# Choose
						current += i_r[next_x][next_y]

						# Explore
						if has_prefix(current):
							search(i_r, board, current, current_lst, next_x, next_y)

						# Un-choose
						board.pop()
						current = current[0:len(current) - 1]

	# When current is in dictionary and length of the word longer than 4, add.
	if current in Word_Dict_Lst and len(current) >= 4:
		if current not in current_lst:
			print('Found: ' + str(current))
			current_lst.append(current)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	# Call the empty list to store all the word in the dictionary.
	global Word_Dict_Lst

	# Open the dictionary file.
	with open(FILE, 'r') as f:

		# Loop over the dictionary.txt.
		for line in f:
			word = line.strip('\n')  # Clean the line up.
			Word_Dict_Lst += [word]  # Add the word to the dictionary list.


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	# Loop over the dictionary.
	global Word_Dict_Lst
	for d_word in Word_Dict_Lst:

		# If the sub string is in the dictionary, return True.
		if d_word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
