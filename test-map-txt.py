#!/usr/bin/env python3

import math
import numpy as np

from bioregions import Bioregions

bioregions=Bioregions()

# Global Map (smaller than above)
print('     '+''.join(['{:+04d}'.format(a) for a in range(-180,180,10)]))
for latitude in range(85,-90,-5):
    line='{:3d}: '.format(latitude)
    for longitude in range(-180,180,10):
        b=bioregions.at(longitude,latitude)
        if len(b)>0:
            txt='{:4s}'.format(b[0])            
        else:
            txt='    '
        line+=txt
    print(line)
