#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from scipy.stats import linregress
from scipy import curve_fit
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
# mpl.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
mpl.rcParams['font.size'] = 16

colours = {
    "green": "#00B828",
    "yellow": "#FFD900",
    "purple": "#800FF2",
    "blue": "#0073FF",
    "orange": "#FF5000",
    "grey": "#B3B3B3",
}
plt.rcParams.update({
    'xtick.major.width': 1.5,     # x-tick thickness
    'ytick.major.width': 1.5,     # y-tick thickness
    'xtick.major.size': 5,        # x-tick length
    'ytick.major.size': 5,        # y-tick length
    'axes.linewidth': 1,         # Thickness of axis border (applies to spines)
    'lines.linewidth': 2
})
