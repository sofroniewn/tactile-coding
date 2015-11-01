"""
Plotting functions associated with the paper in http://github.com/sofroniewn/paper.tuning
"""

from colorsys import hsv_to_rgb, rgb_to_hsv
from numpy import isnan, min, max, where, nan, linspace, asarray, ceil, array, nanmax, arange
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import UnivariateSpline

sns.set_context('paper', font_scale=2.0)
sns.set_style('ticks')

def hist(vals, bins=10, horizontal=False, xlabel=None, ylabel=None, xinvert=False, yinvert=False):
    """
    Plot a histogram with simple formatting options
    """
    if horizontal:
        orientation = 'horizontal'
    else:
        orientation = 'vertical'
    plt.hist(vals, bins=bins, rwidth=0.8, color=[0.7,0.7,0.7], edgecolor='none', orientation=orientation)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if xinvert:
        plt.gca().invert_xaxis()
    if yinvert:
        plt.gca().invert_yaxis()
    sns.despine()

def scatter(x, y, equal=False, xlabel=None, ylabel=None, xinvert=False, yinvert=False):
    """
    Plot a scatter with simple formatting options
    """
    plt.scatter(x, y, 200, color=[0.3, 0.3, 0.3], edgecolors='white', linewidth=1, zorder=2)
    sns.despine()
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if equal:
        plt.axes().set_aspect('equal')
        bmin = min([x.min(), y.min()])
        bmax = max([x.max(), y.max()])
        plt.plot([min(bmin,0), bmax], [min(bmin,0), bmax], color=[0.6, 0.6, 0.6], zorder=1)
        rng = abs(bmax - bmin)
        plt.xlim([bmin - rng*0.05, bmax + rng*0.05])
        plt.ylim([bmin - rng*0.05, bmax + rng*0.05])
    else:
        xrng = abs(x.max() - x.min())
        yrng = abs(y.max() - y.min())
        plt.xlim([x.min() - xrng*0.05, x.max() + xrng*0.05])
        plt.ylim([y.min() - yrng*0.05, y.max() + yrng*0.05])
    if xinvert:
        plt.gca().invert_xaxis()
    if yinvert:
        plt.gca().invert_yaxis()

def smoothfit(x, y, smooth=0, res=1000):
    """
    Smooth data of the form f(x) = y with a spline
    """
    z = y.copy()
    w = isnan(z)
    z[w] = 0
    spl = UnivariateSpline(x, z, w=~w)
    spl.set_smoothing_factor(smooth)
    xs = linspace(min(x), max(x), res)
    ys = spl(xs)
    ys[ys < 0] = 0
    if w[0]:
        if len(where(~w)[0]):
            first = where(~w)[0][0]
            first = x[first]
            first = where(xs >= first)[0][0]-1
            ys[:first] = nan
    if w[-1]:
        if len(where(~w)[0]):
            last = where(~w)[0][-1]
            last = x[last]
            last = where(xs >= last)[0][0]+1
            ys[last:] = nan
    return xs, ys

def smootharray(vals, smooth=0, res=1000):
    """
    Smooth all data in an array
    """
    smoothed = [smoothfit(x, y, smooth=smooth, res=res)[1] for x, y in vals]
    normed = asarray([f/nanmax(f) for f in smoothed])
    return normed

def tuning(x, y, err=None, smooth=None, ylabel=None, pal=None, label='Wall distance (mm)'):
    """
    Plot a tuning curve
    """
    if smooth is not None:
        xs, ys = smoothfit(x, y, smooth)
        plt.plot(xs, ys, linewidth=4, color='black', zorder=1)
    else:
        ys = asarray([0])
    if pal is None:
        pal = sns.color_palette("husl", n_colors=len(x) + 6)
        pal = pal[2:2+len(x)][::-1]
    plt.scatter(x, y, s=300, linewidth=0, color=pal, zorder=2)
    if err is not None:
        plt.errorbar(x, y, yerr=err, linestyle="None", ecolor='black', zorder=1)
    plt.xlabel(label)
    plt.ylabel(ylabel)
    plt.xlim([-2.5,32.5])
    errTmp = err
    errTmp[isnan(err)]  = 0
    rng = max([nanmax(ys), nanmax(y + errTmp)])
    plt.ylim([0 - rng*0.1, rng + rng*0.1])
    plt.yticks(linspace(0,rng,3))
    plt.xticks(range(0,40,10));
    sns.despine()
    return rng

def colormap(sat=None):
    pal = sns.color_palette("husl", n_colors=256)
    pal = pal[32:180][::-1]
    if sat is None:
        hsv = map(lambda x: [x[0], x[1]*1, 1], [rgb_to_hsv(x[0], x[1], x[2]) for x in pal])
    else:
        hsv = map(lambda x: [x[0], x[1]*.6, .9], [rgb_to_hsv(x[0], x[1], x[2]) for x in pal])            
    rgb = [hsv_to_rgb(x[0], x[1], x[2]) for x in hsv]
    pal = ListedColormap(rgb, name='husl')
    return pal

def colorbar(pal):
    """
    Plot a colorbar
    """
    plt.imshow(asarray([arange(20),arange(20),arange(20)]).T, cmap=pal);
    plt.xticks([])
    plt.yticks([])
    plt.gca().invert_yaxis()
    sns.despine()

def time(t, y):
    """
    Plot a time trace for data y = f(t)
    """
    plt.plot(t, y, linewidth=4, color='black')
    sns.despine()

def pairedtime(t1, y1, t2, y2):
    """
    Generate two time traces side by side
    """
    ymax = max([max(y1), max(y2)])
    ymax += 0.05 * ymax
    plt.subplot(1, 2, 1)
    plt.plot(t1, y1, linewidth=4, color='black')
    plt.xlim((-.05, 1.05))
    plt.ylim((-.05*ymax, ymax*1.05))
    plt.ylabel('Spikes / s')
    plt.xlabel('Time (s)')
    plt.xticks([0, 0.5, 1.0])
    plt.subplot(1, 2, 2)
    plt.plot(t2, y2, linewidth=4, color='black')
    plt.xlim((-.05, 1.05))
    plt.ylim((-.05*ymax, ymax*1.05))
    plt.xlabel('Time (s)')
    plt.xticks([0, 0.5, 1.0])
    sns.despine()
    plt.gca().get_yaxis().set_visible(False)

def heatmap(vals, size=6, aspect=1, vmin=0, vmax=1):
    """
    Plot a heatmap from matrix data
    """
    plt.figure(figsize=(size,size))
    plt.imshow(vals, cmap='gray', aspect=aspect, interpolation='none', vmin=vmin, vmax=vmax)
    plt.axis('off')

def pairedheatmap(vals1, vals2, size=6, aspect=1):
    """
    Plot two heatmaps side by side
    """
    plt.figure(figsize=(size,size))
    plt.subplot(1, 2, 1)
    plt.imshow(vals1, cmap='gray', aspect=aspect, interpolation='none', vmin=0, vmax=1)
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(vals2, cmap='gray', aspect=aspect, interpolation='none', vmin=0, vmax=1)
    plt.axis('off')