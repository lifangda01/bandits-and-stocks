from pylab import *
from stocks import *
import egreedy_stocks
import ucb1_stocks
import thompson_stocks
import exp3_stocks
import random_stocks

# TODO: box plot of reward, progression of avg cumulative reward, % of best arm pulled

def main():
	f500_stock_table = 'stocks/fortune-500.csv'
	rand_stock_table = 'stocks/random-stocks.csv'
	table = readInStockTable(rand_stock_table)
	payoffGraph(table, list(sorted(table.keys())), cumulative=True)

	expDict = {}
	expDict['egreedy'] = egreedy_stocks.runExperiment
	expDict['ucb1'] = ucb1_stocks.runExperiment
	expDict['thompson'] = thompson_stocks.runExperiment
	expDict['exp3'] = exp3_stocks.runExperiment
	expDict['random'] = random_stocks.runExperiment

	numRuns = 100
	allRewards = []
	allAvgRewards = []

	# Epsilon-greedy: epsilon = 0.05
	# UCB1
	# Thompson sampling
	# Exp3: gamma = 0.5
	# Random
	for m in expDict:
		print m
		rewards = []
		for i in range(numRuns):
			reward, bestActionReward, bestStock, avgRewards = expDict[m](table)
			rewards.append(reward)
		allRewards.append(rewards)
	# Whisker plot
	figure()
	boxplot(allRewards, labels=[m for m in expDict])
	title('Reward Over %d Runs' % (numRuns))
	xlabel('Methods')
	ylabel('Reward')
	show()

if __name__ == '__main__':
	main()