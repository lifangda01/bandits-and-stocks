from egreedy.egreedy import epsilon_greedy
from stats import stats
from stocks import *
from random import shuffle

def eGreedyStocks(stockTable, epsilon=0.05):
	tickers = list(stockTable.keys())
	shuffle(tickers) # note that this makes the algorithm SO unstable
	numRounds = len(stockTable[tickers[0]])
	numActions = len(tickers)
	avgRewards = []

	reward = lambda choice, t: payoff(stockTable, t, tickers[choice])
	singleActionReward = lambda j: sum([reward(j,t) for t in range(numRounds)])

	bestAction = max(range(numActions), key=singleActionReward)
	bestActionCumulativeReward = singleActionReward(bestAction)

	cumulativeReward = 0
	t = 0
	generator = epsilon_greedy(numActions, reward, epsilon)
	for (chosenAction, reward) in generator:
		cumulativeReward += reward
		t += 1
		avgRewards.append(cumulativeReward * 1.0 / t)
		if t == numRounds:
			break

	return cumulativeReward, bestActionCumulativeReward, tickers[bestAction], avgRewards

def runExperiment(table, epsilon=0.05):
	reward, bestActionReward, bestStock, avgRewards = eGreedyStocks(table, epsilon)
	print("For a single run: ")
	print("Payoff was %.2f" % reward)
	print("Regret was %.2f" % (bestActionReward - reward))
	print("Best stock was %s at %.2f" % (bestStock, bestActionReward))
	return reward, bestActionReward, bestStock, avgRewards

if __name__ == "__main__":
	table = readInStockTable('stocks/fortune-500.csv')
	runExperiment(table)
	payoffGraph(table, list(sorted(table.keys())), cumulative=True)

	# print()

	# table2 = readInStockTable('stocks/random-stocks.csv')
	# runExperiment(table2)
	# payoffGraph(table2, list(sorted(table2.keys())), cumulative=True)

