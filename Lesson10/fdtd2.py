import multiprocessing

from avgNumOfSteps import avg_num_of_steps
import pandas as pd


def from_dict_to_dfs2(file_name: multiprocessing.Queue, output: multiprocessing.Queue) -> None:
    for files in iter(file_name.get, None):
        output.put(pd.DataFrame.from_dict(avg_num_of_steps("out/" + files), orient='index'))
