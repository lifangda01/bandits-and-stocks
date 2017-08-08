import math
import random

def epsilon_greedy(numActions, reward, epsilon=0.05):
	payoffSums = [0.0] * numActions
	numPlays = [1] * numActions

	# initialize empirical means
	for t in range(numActions):
		payoffSums[t] = reward(t,t)
		yield t, payoffSums[t]

	t = numActions

	while True:
		empMeans = [payoffSums[i] / numPlays[i] for i in range(numActions)]
		action = max(range(numActions), key=lambda i: empMeans[i])
		if random.uniform(0, 1) < 0.05:
			arms = range(numActions)
			arms[action], arms[-1] = arms[-1], arms[action]
			action = arms[:-1][random.randint(0, numActions-2)]
		theReward = reward(action, t)
		numPlays[action] += 1
		payoffSums[action] += theReward

		yield action, theReward
		t = t + 1