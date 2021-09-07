#!/usr/bin/env python3

from bioregions import Bioregions
import matplotlib.pyplot as plt
from multiprocessing import Pool
import numpy as np
import random

bioregions=Bioregions()

# Random colour for each region
random.seed(23)
codes={
    region.code()
    :
    [
        random.uniform(0.1,1.0),
        random.uniform(0.1,1.0),
        random.uniform(0.1,1.0)
    ]
    for region in bioregions._bioregions
}

# Returns a row of pixels for a given latitude
def mapRow(latitude):
    print('.',end='',flush=True)
    rowpixels=[]
    for longitude in np.arange(-180.0,180.0,1.0):
        b=bioregions.at(longitude,latitude)
        if len(b)>0:
            rowpixels.append(codes[b[0]])
        else:
            rowpixels.append([0,0,0])
    return rowpixels

# Map rows in parallel
pixels=np.array(
    Pool().map(
        mapRow,
        np.arange(89.0,-90.0,-1.0)
    )
)
print()

plt.figure()
plt.imshow(pixels)
plt.axis('off')
plt.show()
