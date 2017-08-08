from stocks import *
import egreedy_stocks
import ucb1_stocks
import thompson_stocks
import exp3_stocks

# TODO: box plot of reward, progression of avg cumulative reward, % of best arm pulled

def main():
	table = readInStockTable('stocks/fortune-500.csv')
	payoffGraph(table, list(sorted(table.keys())), cumulative=True)
	# Epsilon-greedy
	egreedy_stocks.runExperiment(table)
	# UCB1
	ucb1_stocks.runExperiment(table)
	# Thompson sampling
	thompson_stocks.runExperiment(table)
	# Exp3
	gamma = 0.33
	exp3_stocks.runExperiment(table, gamma)

if __name__ == '__main__':
	main()