from avgNumOfSteps import avg_num_of_steps
import pandas as pd


def from_dict_to_dfs2(file_name, output):
	# return output.put(pd.DataFrame.from_dict(avg_num_of_steps("out/" + file_name), orient='index'))
	return output.put(set(avg_num_of_steps("out/" + file_name)))

