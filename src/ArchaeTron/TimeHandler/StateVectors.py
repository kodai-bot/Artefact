import pandas as pd
import numpy as np
import math
import geopandas as gpd
from shapely.geometry import Point
from TimeHandler.positionCalculator import positionCalculator
from TimeHandler.to_Cartesian import to_cartesian

# This class is used to store the state vectors of a moving object with changing properties
# The state vector is a list of dictionaries, each dictionary represents the state of the object at a given time

class StateVector:
    def __init__(self):
        self.vector = []

    def add_previous_state(self, object):
        self.vector.append(object)

    def get_state(self, index):
        if 0 <= index < len(self.vector):
            return self.vector[index]
        else:
            raise IndexError("Index out of range, the object does not exist at this index")
        
    # x,y,z are lat long and distance from earth along an imaginary line. Epoch used if necessary is j2000.
    # the latitude, longitude are those of the object being appended and the distance is the number of years #before or after j2000. 

    def add_state(self, t, ra, dec, z_0, object_details, inception_point):
        self.vector[t] = {
            'RA': ra,
            'Dec': dec,
            'z_0': z_0,
            'object_details': object_details,
            'inception_point': inception_point
        }

    def get_state(self, t):
        return self.vector[t]
    
    





#t=0: [x_0, y_0, z_0, "A"]
#t=1: [x_1, y_1, z_1, "A"]
#t=2: [x_2, y_2, z_2, "A"]
#t=3: [x_3, y_3, z_3, "A"]
#t=4: [x_4, y_4, z_4, "A"]
#t=5: [x_5, y_5, z_5, "B"]
#t=6: [x_6, y_6, z_6, "B"]
#t=7: [x_7, y_7, z_7, "B"]
#t=8: [x_8, y_8, z_8, "B"]
#t=9: [x_9, y_9, z_9, "B"]
#t=10: [x_10, y_10, z_10, "A"]
#t=11: [x_11, y_11, z_11, "A"]
##t=12: [x_12, y_12, z_12, "A"]

#t=0: [RA, Dec, z_0, "A"]
#t=1: [RA, Dec, z_1, "A"]
#t=2: [RA, Dec, z_2, "A"]
#t=3: [RA, Dec, z_3, "A"]
#t=4: [RA, Dec, z_4, "A"]
#t=5: [RA, Dec, z_5, "B"]

...

#t=0: [RA, Dec, z_0, "A", "Entity1", "Rotational Symmetry"]
#t=1: [RA, Dec, z_1, "A", "Entity1", "Rotational Symmetry"]
#t=2: [RA, Dec, z_2, "A", "Entity1", "Rotational Symmetry"]
#t=3: [RA, Dec, z_3, "A", "Entity1", "Rotational Symmetry"]
#t=4: [RA, Dec, z_4, "A", "Entity1", "Rotational Symmetry"]
#t=5: [RA, Dec, z_5, "B", "Entity1", "Rotational Symmetry"]

#t=18: [RA, Dec, z_18, "B", "Entity1", "Rotational Symmetry"]
#t=19: [RA, Dec, z_19, "B", "Entity1", "Rotational Symmetry"]
#t=20: [RA, Dec, z_20, "None", "Entity1", "None"]
