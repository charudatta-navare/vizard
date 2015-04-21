#!/usr/bin/env python
from __future__ import division

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colorbar as cbar
import matplotlib.colors as mcolors
import cartopy
import cartopy.io.shapereader as shpreader
from collections import defaultdict
from sys import argv
from re import sub
import shapely
import math
import cartopy.crs as ccrs

__author__ = "Charudatta Navare"
__credits__ = ["Charudatta Navare"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Charudatta Navare"
__email__ = "charudatta.navare@gmail.com"

from tempfile import NamedTemporaryFile
from unittest import TestCase, main
from vizard import (normalize_color_values,
verify_geo_coordinates, plot_world_map)


class WorkflowTests(TestCase):

    def setUp(self):
        """setup the test values"""
        self.test_data = test_data
        self.coordinates_data = coordinates_data

    def tearDown(self):
        pass
        """remove all the files after completing tests """

    def test_plot_world_map(self):

        in_data = self.test_data.split('\n')
        feature_value = defaultdict(float)
        exists_c = defaultdict(str)
        for line in in_data:
            cols = line.split('\t')
            try:
                country_name = cols[0]
                val = cols[3]
                val = val.rstrip()
                country_name = country_name.rstrip()
                country_name = sub(r'^"|"$', '', country_name)
                feature_value[country_name] = float(val)
            except IndexError:
                pass
        actual = plot_world_map(feature_value, outpng='out.png')
        expected = None
        self.assertEqual(actual, expected)

    def test_verify_geo_coordinates(self):
        coords_data = self.coordinates_data.split('\n')
        coords = list()
        for line in coords_data:
            cols = line.split(',')
            longitude = str(cols[0])
            latitude = str(cols[1])
            coord = list([longitude, latitude])
            coords.append(coord)
        ver_coords = verify_geo_coordinates(coords)
        expected = list([[112, 38], [38, 4], [27, -27], [-34, 54]])
        self.assertEqual(ver_coords, expected)

        coords = list([['181E', '3N'], ['145E', '45N']])
        expected = list([[145, 45]])
        ver_coords = verify_geo_coordinates(coords)
        self.assertEqual(ver_coords, expected)

test_data = """
Malaysia	var_code	var_name 	1.47384615385	0.572738898141
Peru	var_code	var_name 	1.89267886855	0.77811209326
Chile	var_code	var_name 	1.91574724173	0.643879719106
Yemen	var_code	var_name 	2.135	0.73845806944
China	var_code	var_name 	1.99383802817	0.584518353133
New Zealand	var_code	var_name 	1.71306471306	0.580416138938
Cyprus	var_code	var_name 	1.91482965932	0.763878952587
Philippines	var_code	var_name 	1.61416666667	0.696924715402
Ecuador	var_code	var_name 	1.5	0.648125459427
Japan	var_code	var_name 	1.78444632291	0.651577245492
Palestine	var_code	var_name 	2.20481927711	0.693267601512
Germany	var_code	var_name 	1.90976331361	0.641627296614
Belarus	var_code	var_name 	2.23707787733	0.691048783247
Kazakhstan	var_code	var_name 	1.79933333333	0.631927562187
Estonia	var_code	var_name 	2.13121272366	0.634977328234
Egypt	var_code	var_name 	3.06040709127	0.940560177678
Lebanon	var_code	var_name 	2.05443886097	0.674938433774
Bahrain	var_code	var_name 	2.11789297659	0.821457572967
Uruguay	var_code	var_name 	1.81306532663	0.712937465513
Spain	var_code	var_name 	1.99747048904	0.568507121529
Hong Kong	var_code	var_name 	1.88677354709	0.609359802521
Ghana	var_code	var_name 	1.66043814433	0.830608401869
Romania	var_code	var_name 	2.23010033445	0.723873581376
Iraq	var_code	var_name 	2.25567703953	0.706078812561
Jordan	var_code	var_name 	1.98	0.69642240784
Morocco	var_code	var_name 	2.06015037594	0.768130452517
Colombia	var_code	var_name 	1.52349437459	0.662583719415
Netherlands	var_code	var_name 	1.75106157113	0.588547036216
Tunisia	var_code	var_name 	2.08569051581	0.712779665593
Pakistan	var_code	var_name 	1.75125208681	0.830633783785
Sweden	var_code	var_name 	1.63092269327	0.584128455981
Qatar	var_code	var_name 	1.45849056604	0.54554040997
Zimbabwe	var_code	var_name 	1.77666666667	0.790277534336
Poland	var_code	var_name 	1.84332281809	0.530793943462
Nigeria	var_code	var_name 	1.6549175668	0.846439025181
South Africa	var_code	var_name 	1.87325944871	0.87467588639
Taiwan	var_code	var_name 	1.8295269168	0.615030197109
Brazil	var_code	var_name 	1.73939393939	0.626323641261
Singapore	var_code	var_name 	1.69523326572	0.614320557763
Thailand	var_code	var_name 	1.6875	0.645645257216
Mexico	var_code	var_name 	1.387	0.608618277826
Turkey	var_code	var_name 	1.8153942428	0.785171471857
Algeria	var_code	var_name 	2.05555555556	0.711462077508
Trinidad and Tobago	var_code	var_name 	1.58758758759	0.720502834662
United States	var_code	var_name 	1.73693693694	0.640516905938
Slovenia	var_code	var_name 	1.98303487276	0.641118294584
Argentina	var_code	var_name 	1.81943081452	0.665435784854
Azerbaijan	var_code	var_name 	1.94211576846	0.717027604758
Armenia	var_code	var_name 	1.91758241758	0.799049858307
Australia	var_code	var_name 	1.69672131148	0.587721402731
Uzbekistan	var_code	var_name 	1.38847957133	0.561667524366
Kuwait	var_code	var_name 	1.66666666667	0.639206904508
India	var_code	var_name 	1.89974619289	0.828139969182
Russia	var_code	var_name 	2.10146137787	0.664892653812
Kyrgyzstan	var_code	var_name 	1.68024032043	0.555434145364
South Korea	var_code	var_name 	1.95663052544	0.53566053596
Rwanda	var_code	var_name 	1.70006548788	0.665883656656
Libya	var_code	var_name 	1.78256750355	0.744394051781
Ukraine	var_code	var_name 	2.16549789621	0.759936514659
"""

coordinates_data = """112E,38N,Zhoukoudian
38E,4N
27E,27S
34W,54N"""

# run tests if called from command line
if __name__ == '__main__':
    main()
