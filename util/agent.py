from environment import *
from collections import defaultdict

def dp_algo(ob_file, H, V, I, T):
	c = defaultdict(list)
	env = Environment(ob_file, setup=False)
	steps = H / T
	for i in range(0, T)[::-1]:
		for j in range(i, T):
			env.get_timesteps(j, T)
			
			
if __name__ == "__main__":
	dp_algo("../LOBSTER_SampleFile_MSFT_2012-06-21_1/MSFT_2012-06-21_34200000_57600000_orderbook_1.csv", 10, 10000, 10, 10	)
