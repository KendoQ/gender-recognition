#!/usr/bin/enyv python 

# file: findceps.py (Python 2.7)

# Author: Daniel Douglas

# Purpose: Extract cepstral coefficients 

# Function imports
import numpy as np
from sys import argv
from speech import *
import matplotlib.pyplot as plt
import pylab

# Find the mel frequency cepstral coefficients of a signal
def findceps(x, n=None):
    
    # Unwrap the phase of the spectrum
    def _unwrap(phase):
        # unwrap phase
        samples = phase.shape[-1]
        unwrapped = np.unwrap(phase)

        # find the center frequency
        center = (samples+1)//2
        if samples == 1: 
            center = 0  

        # unwrap the phase of the center frequency
        ndelay = np.array(np.round(unwrapped[...,center]/np.pi))

        # unwrap the phase of the other frequencies
        unwrapped -= np.pi * ndelay[...,None] * np.arange(samples) / center

        # return the unwrapped phase and the delay
        return unwrapped, ndelay
    # end _unwrap

    # compute the specstrum with FFT
    spectrum = np.fft.fft(x, n=n)
    unwrapped_phase, ndelay = _unwrap(np.angle(spectrum))

    # compute the log spectrum
    log_spectrum = np.log(np.abs(spectrum)) + 1j*unwrapped_phase

    # compute the cepstrum
    ceps = np.fft.ifft(log_spectrum).real

    # return the coefficients and the delay
    return ceps, ndelay

""" sound = Speech(argv[1])
ceps, _ = findceps(sound.signal, 1000)

duration = 1.0
samples = int(sound.fs*duration)
t = np.arange(samples) / sound.fs
print t.shape
print ceps.shape
plt.plot(t[:ceps.shape[0]], ceps)
pylab.show()
 """