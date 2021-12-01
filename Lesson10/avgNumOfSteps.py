import pandas as pd

def avg_num_of_steps(file_name: str) -> dict:
	df = pd.read_csv(file_name, delimiter=";")
	grouped_df = df.groupby("tag")
	sum_of_steps = grouped_df.sum()["n_steps"]
	count_of_steps = grouped_df.count()["n_steps"]
	avg = sum_of_steps/count_of_steps
	return avg.to_dict()

