import random
from scipy import stats

def thompson_sampling(numActions, reward, bestReward, worstReward):
	payoffSums = [0.0] * numActions
	numPlays = [1] * numActions
	success = [1] * numActions
	failure = [1] * numActions
	t = 0

	while True:
		theta = [stats.beta(success[i], failure[i]).rvs() for i in range(numActions)]
		action = max(range(numActions), key=lambda i: theta[i])
		theReward = reward(action, t)
		numPlays[action] += 1
		payoffSums[action] += theReward

		if t == 1300: print success, failure

		yield action, theReward
		t = t + 1

		scaledReward = (theReward - worstReward) / (bestReward - worstReward)

		if random.uniform(0, 1) < scaledReward:
			success[action] += 1
		else:
			failure[action] += 1
