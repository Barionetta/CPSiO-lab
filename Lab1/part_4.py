# -*- coding: utf-8 -*-
"""
    Skrypt zawierający rozwiązanie zadania czwartego z laboratorium 1
"""
__version__ = '1.0.0'
__author__ = 'Mateusz Gawłowski, Katarzyna Matuszek'

import argparse
from pathlib import Path
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="signal's filename. Must be in 'data' directory.")
    args = parser.parse_args()

    filename = args.file
    path = Path.cwd().parent.joinpath("data", filename)
    signal = np.loadtxt(path)
    samples, signal = signal.T

    lenght = len(signal)
    normalize = lenght / 2
    freq_domain = np.fft.fftfreq(lenght, samples[-1])
    fsignal = fft(signal)
    inv_signal = ifft(fsignal)

    sns.set_theme(palette="colorblind", style="whitegrid", context="paper")
    fig = plt.figure(figsize=(16,9))
    fig.suptitle("Sygnał i jego przekształcenia")
    gs = plt.GridSpec(nrows=3, ncols=1)
    fig.add_subplot(gs[0,0])
    sns.lineplot(x=samples, y=signal, legend=None, color='C0').set(xlabel="Czas [s]", ylabel="Sygnał", title="Sygnał sinusoidalny")
    fig.add_subplot(gs[1,0])
    sns.lineplot(x=freq_domain, y=np.abs(fsignal)/normalize, legend=None, color='C1').set(xlabel="Częstotliwość [Hz]", ylabel="Amplituda", title="Widmo amplitudowe sygnału po transformacji Fouriera")
    fig.add_subplot(gs[2,0])
    sns.lineplot(x=samples, y=inv_signal, legend=None, color='C2').set(xlabel="Czas [s]", ylabel="Sygnał", title="Sygnał po odwrotnej transformacji Fouriera")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()