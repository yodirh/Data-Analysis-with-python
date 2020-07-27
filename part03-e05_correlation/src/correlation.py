#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("D:\DA Helsinki\iris.csv").drop('species', axis=1).values

def lengths():
    i = load()
    return scipy.stats.pearsonr(i[:,0],i[:,2])[0]

def correlations():
    i = load()
    j = np.corrcoef(i, rowvar=False)
    return np.array(j)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
