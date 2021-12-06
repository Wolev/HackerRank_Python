''' Find the runner-up score and the max score from a random generated array of positive integers. '''

import random

def runner_up(array):
	maxscore = 0
	runner_up = 0
	for i in array:
		if i > maxscore:
			maxscore, runner_up = i, maxscore
		elif maxscore > i and runner_up < i:
			runner_up = i
	print("The max score is: " + str(maxscore))
	print("The runner_up is: " + str(runner_up))

print("Input the number of array elements: ")
n = int(input())

print("Generating an array...")
array = random.sample(range(1,10), n)
print("Array generated : " + str(array))

runner_up(array)
