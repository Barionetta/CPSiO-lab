import argparse
from pathlib import Path
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="signal's filename. Must be in 'data' directory.")
    args = parser.parse_args()

    filename = args.file
    path = Path.cwd().parent.joinpath("data", filename)
    signal = np.loadtxt(path)

    sns.set_theme()
    sns.relplot(data=signal, kind='line', palette="bright").set(xlabel="Numer próbki [n]", ylabel="Wartość", title="Sygnał EKG")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()