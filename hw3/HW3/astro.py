__author__ = 'Suota'

import ephem
from HW3 import download
import matplotlib.pyplot as plt
from datetime import date
from HW3 import download

today = date.today()
year_ago = (date.today().year - 1, date.today().month , date.today().day)
pos_ra = []
pos_dec = []
distance = []
planet_set = False


def set_planet(name):

    # plotting one of planets x is time : days and y is distance from Earth

    global planet_set
    planet_set = True

    del distance[:]

    if download.one_month:
        time = 30
    elif download.one_week:
        time = 7
    else :
        time = 365
# setting appropriate number of days

# creating a list of everyday distance between the planet and Earth

    if name=="mars":
        for i in range (0,time):
            day = (date.today().year, date.today().month , date.today().day-i)
            m = ephem.Mars(day)
            distance.append(m.earth_distance)
    elif name=="jupiter":
        for i in range (0,time):
            day = (date.today().year, date.today().month , date.today().day-i)
            m = ephem.Jupiter(day)
            distance.append(m.earth_distance)
    elif name=="moon":
        for i in range (0,time):
            day = (date.today().year, date.today().month , date.today().day-i)
            m = ephem.Moon(day)
            distance.append(m.earth_distance)
    elif name=="saturn":
        for i in range (0,time):
            day = (date.today().year, date.today().month , date.today().day-i)
            m = ephem.Saturn(day)
            distance.append(m.earth_distance)

    ax2 = download.fig.add_subplot(121)
    ax2.set_title(name)
    ax2.plot(range(time),distance, color='blue', label='the data')

    plt.show()


def set_mars():
    set_planet("mars")


def set_jupiter():
    set_planet("jupiter")


def set_moon():
    set_planet("moon")


def set_saturn():
    set_planet("saturn")