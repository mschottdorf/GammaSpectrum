# GammaSpectrum
Code to plot the Gamma spectrum

# Format of the raw data

The files "counts.dat" contains the gamma spectroscopy raw data. It contains two columns of the format
```
channel count
0 0
1 0
2 10
```
The channel number is linearly related to the energy. The best fit is
```
$ENER_FIT: -0.187070 0.489660
```
So that `E = a + b*channel` with a = -0.187070 and b = 0.489660.

# Sources of the lines
A subset of the emission lines have been labelled. The energy levels were taken from "The Lund/LBNL Nuclear Data Search" Version 2.0 (1999/2) by S.Y.F. Chu1, L.P. Ekström and R.B. Firestone. The data is available online: http://nucleardata.nuclear.lu.se/toi/

Specific links were left in the source code.

# How to make plot
Just execute `python make_plot.py`

