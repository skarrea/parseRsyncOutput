from pathlib import Path
import argparse
from collections import defaultdict
import pandas as pd

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog = 'Rsync parser',
                        description = 'Parses output from rsync -i'
    )
    parser.add_argument('filename')           # positional argument
    parser.add_argument('-d', '--depth', type=int, default=-1)      # option that takes a value
    args = parser.parse_args()
    rowList = []
    with open(args.filename, 'r') as f:
        lines = [line for line in f.read().split('\n')[1:-3] if line[0:11] == '>f+++++++++']
        files = [line[12:] for line in lines]
    for file in files:
        parts = Path(file).parts
        rowList.append({level : file for level, file in enumerate(parts)})
    fileDF = pd.DataFrame(rowList)
    # import pdb; pdb.set_trace()
    for i, col in enumerate(fileDF.columns[:-1]):
        print(fileDF.value_counts(subset=list(fileDF.columns[:(i+1)])))
    