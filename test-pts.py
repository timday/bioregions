#!/usr/bin/env python3

from bioregions import Bioregions

bioregions=Bioregions(False)  # Use True for verbose loading messages

pts=[
    [ -0.118092, 51.509865,'London'],
    [  2.349014, 48.864716,'Paris'],
    [-73.935242, 40.730610,'New York'],
    [ 11.576124, 48.137154,'Munich'],
    [ 37.618423, 55.751244,'Moscow'],
    [139.839478, 35.652832,'Tokyo'],
    [151.209900,-33.865143,'Sydney'],
    [174.763336,-36.848461,'Auckland']
    ]

for pt in pts:
    codes=bioregions.at(pt[0],pt[1])
    if len(codes)==0:
        print('{} is in no bioregions').format(pt[2])
    for code in codes:
        print(
            '{} is in bioregion {}: {}'.format(pt[2],code,bioregions.descriptionForCode(code))
        )
