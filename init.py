# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# Import the random module for generating random numbers
import random

# Function to simulate a layup shot
def layup(contest, block):
	# Generate a random number between 0 and 1 for the chance of making the shot
	chance = random.random()

	# If the shot is contested, adjust the chance using the contest_shot function
	if contest == True:
		chance = contest_shot(chance)
	
	# If the shot is blocked, check if the block_shot is successful, resulting in a miss
	if block == True and block_shot() == True:
		result = "miss"
	# If the shot is not blocked and the chance is within the make probability, the shot is successful
	elif chance <= 0.95:
		result = "in: 1 point"
	# If the shot is not blocked and the chance is outside the make probability, the shot is a miss
	else:
		result = "miss"

	# Simulate the chance of rebounding the missed shot, and if successful, change the result to a made shot
	rebound = random.random()
	if result == "miss" and rebound <= 0.30:
		result = "REBOUND! in: 1 point"
	return result

# Function to simulate a mid-range shot
def mid_range(contest, block):
	# Generate a random number between 0 and 1 for the chance of making the shot
	chance = random.random()

	# If the shot is contested, adjust the chance using the contest_shot function
	if contest == True:
		chance = contest_shot(chance)
	
	# If the shot is blocked, check if the block_shot is successful, resulting in a miss
	if block == True and block_shot() == True:
		result = "miss"
	# If the shot is not blocked and the chance is within the make probability, the shot is successful
	elif chance <= 0.55:
		result = "in: 2 points"
	# If the shot is not blocked and the chance is outside the make probability, the shot is a miss
	else:
		result = "miss"

	# Simulate the chance of rebounding the missed shot, and if successful, change the result to a made shot
	rebound = random.random()
	if result == "miss" and rebound <= 0.30:
		result = "REBOUND! in: 2 points"
	return result

# Function to simulate a three-point shot
def three(contest, block):
	# Generate a random number between 0 and 1 for the chance of making the shot
	chance = random.random()

	# If the shot is contested, adjust the chance using the contest_shot function
	if contest == True:
		chance = contest_shot(chance)
	
	# If the shot is blocked, check if the block_shot is successful, resulting in a miss
	if block == True and block_shot() == True:
		result = "miss"
	# If the shot is not blocked and the chance is within the make probability, the shot is successful
	elif chance <= 0.35:
		result = "in: 3 points"
	# If the shot is not blocked and the chance is outside the make probability, the shot is a miss
	else:
		result = "miss"

	# Simulate the chance of rebounding the missed shot, and if successful, change the result to a made shot
	rebound = random.random()
	if result == "miss" and rebound <= 0.30:
		result = "REBOUND! in: 3 points"
	return result

# Function to simulate the chance of blocking a shot
def block_shot():
	# Generate a random number between 0 and 1, and if it's within the block probability, the shot is blocked
	chance = random.random()
	if chance <= 0.10:
		return True
	else:
		return False

# Function to adjust the chance of making a shot if it is contested
def contest_shot(chance):
	return (chance + 0.05)

# Get user input for offensive and defensive actions
offensive = input("Enter an offensive action (1 for layup, 2 for mid-range, 3 for three-pointer): ")
defensive = input("Enter a defensive action (C for contest, B for block): ")

# Check the defensive action and set flags accordingly
if defensive == 'c' or defensive == 'C':
	contest = True
	block = False
elif defensive == 'b' or defensive == 'B':
	contest = False
	block = True
else:
	print("Invalid defensive action!")

# Check the offensive action and call the corresponding function
if offensive == '1':
	print(layup(contest, block))
elif offensive == '2':
	print(mid_range(contest, block))
elif offensive == '3':
	print(three(contest, block))
else:
	print("Invalid offensive action!")
