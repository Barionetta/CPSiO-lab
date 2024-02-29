import argparse
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("frequencies", type=int, nargs='+', help="frequencies of signals in Hz")
    parser.add_argument("-f", "--fourier", action="store_true", help="show discrete Fourier Transform of signal")
    parser.add_argument("-i", "--invert", action="store_true", help="show inverted discrete Fourier Transform of signal")
    args = parser.parse_args()

    frequency = 50
    time = np.linspace(0, 1, 65536)
    signal = np.sin(2 * np.pi * frequency * time)

    sns.set_theme()
    sns.lineplot(signal).set(xlabel="Numer próbki [n]", ylabel="Wartość", title="Sinusoida")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()