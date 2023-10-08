import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import 

# Class to visualise the data. 
# This class will be used to visualise the data in the form of graphs and plots.

class GeoDataVisualiser:
    def __init__(self, data):
        self.data = data


    def plot_data(self, geo_data):
        fig, ax = plt.subplots(figsize=(15, 15))
        geo_data.plot(ax=ax)
        plt.show()

    
        
        