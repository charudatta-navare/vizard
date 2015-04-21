#!/usr/bin/env python
from  __future__ import division

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colorbar as cbar
import matplotlib.colors as mcolors
import cartopy
import cartopy.io.shapereader as shpreader
from collections import defaultdict
from sys import argv
from re import sub, compile as recompile
import shapely
import math
import cartopy.crs as ccrs

__author__ = "Charudatta Navare"
__credits__ = ["Charudatta Navare"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charudatta Navare"
__email__ = "charudatta.navare@gmail.com"


def verify_geo_coordinates(geo_coordinates):

    patternS = recompile("S")
    patternW = recompile("W")
    patternE = recompile("E")
    patternN = recompile("N")

    verif_coordinates = list()

    for longitude, latitude in geo_coordinates:

        if patternW.search(longitude):
            longitude = sub('W', '', longitude)
            longitude = -1 * int(longitude)
            longitude = int(longitude)

        elif patternE.search(longitude):
            longitude = sub('E', '', longitude)
            longitude = int(longitude)

        if patternS.search(latitude):
            latitude = sub('S', '', latitude)
            latitude = -1 * int(latitude)
            latitude = int(latitude)

        elif patternN.search(latitude):
            latitude = sub('N', '', latitude)
            latitude = int(latitude)
        try:
            if abs(latitude) <= 90 and abs(longitude) <= 180:
                coords = list([longitude, latitude])
                verif_coordinates.append(coords)
        except TypeError:
            pass

    return verif_coordinates


def plot_world_map(input_dict, coordinates=None,
                   outpng='world_map.png', suptitle='Super Title',
                   title='Title', text='text'):

    fig, ax = plt.subplots(figsize=(12, 6),
                           subplot_kw={'projection': ccrs.PlateCarree()})

    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
    ax.set_extent([-150, 60, -25, 60])
    shpfilename = './world/world'
    reader = shpreader.Reader(shpfilename)
    countries = reader.records()
    cmap = plt.cm.Greens
    input_dict = normalize_color_values(input_dict)

    for country in countries:
        name = str(country.attributes['NAME'])
        try:
            color_int = input_dict[name]
            if type(color_int) == int:
                ax.add_geometries(
                    country.geometry, ccrs.PlateCarree(),
                    facecolor=cmap(color_int))
            else:
                ax.add_geometries(
                    country.geometry, ccrs.PlateCarree(), facecolor='#D2B48C')
        except ValueError:
            ax.add_geometries(
                country.geometry, ccrs.PlateCarree(), facecolor='#D2B48C')
        except TypeError:
            ax.add_geometries(
                country.geometry, ccrs.PlateCarree(), facecolor='#D2B48C')

    if coordinates is not None:
        geo_coordinates = verifiy_geo_coordinates(coordinates)
        for lon, lat in geo_coordinates:
            ax.scatter(lon, lat, c=(0, 0, 0), transform=ccrs.PlateCarree())

    fig.text(0.14, 0.05, text, color='black', bbox=dict(
        facecolor='none', edgecolor='none', boxstyle='round,pad=1'))

    norm = mcolors.Normalize(vmin=1, vmax=10)
    cax = fig.add_axes([0.95, 0.2, 0.02, 0.6])
    cb = cbar.ColorbarBase(cax, cmap=cmap, norm=norm, spacing='proportional')

    plt.suptitle(suptitle, fontsize=18)
    ax.set_title(title)
    plt.savefig(outpng)
    return None


def normalize_color_values(feature_value):

    val_list = list(feature_value.values())
    max_val = max(val_list)
    min_val = min(val_list)

    for key in feature_value:
        val = feature_value[key]
        val = 255.0 * (val - min_val) / (max_val - min_val)
        feature_value[key] = int(round(val))

    return feature_value
