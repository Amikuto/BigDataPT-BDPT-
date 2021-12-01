import pandas as pd

from avgNumOfSteps import avg_num_of_steps

def from_dict_to_dfs(file_name):
	return pd.DataFrame.from_dict(avg_num_of_steps("out/" + file_name), orient='index')

