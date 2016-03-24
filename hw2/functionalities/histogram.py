__author__ = 'Suota'

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


def set_hist():

    im = misc.lena()                                      # get example image

    hist, bin_edges = np.histogram(im, bins=65)     # creating histogram : array with values of histogram and bin edges

    bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])

    plt.figure(figsize=(8,4))                       # creating new figure of figsize width ang height

    plt.subplot(121)                                # positioning subplot : 1-rows , 2- cols , 1- plot number
    plt.axis('off')                                 # displaying without axis
    plt.imshow(im)

    plt.subplot(122)
    plt.plot(bin_centers, hist)                                                     # positioning histogram
    plt.text(0.57, 0.8, 'histogram', fontsize=15, transform = plt.gca().transAxes)  # adding name 'histogram'

    plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)  # adding and positioning subplots
    plt.show()

    misc.imsave('example.gif', im)                     # saving used image to file
