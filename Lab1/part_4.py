import argparse
from pathlib import Path
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import signal

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="signal's filename. Must be in 'data' directory.")
    args = parser.parse_args()

    filename = args.file
    path = Path.cwd().parent.joinpath("data", filename)
    print(path)

if __name__ == "__main__":
    main()