import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import folium

#from sklearn import KMeans
#from sklearn.decomposition import PCA
#from sklearn.preprocessing import StandardScaler

# Class to visualise the data. 
# This class will be used to visualise the data in the form of graphs and plots.

class GeoDataVisualiser:
    def __init__(self):
        pass

    # Plot the data using matplotlib
    def plot_data(self, geo_data):
        fig, ax = plt.subplots(figsize=(15, 15))
        geo_data.plot(ax=ax)
        plt.show()

    # Plot the data using matplotlib with colours
    def plot_data_with_colours(self, geo_data, column):
        fig, ax = plt.subplots(figsize=(15, 15))
        geo_data.plot(ax=ax, column=column, legend=True)
        plt.show()


    def plot_data_combined(self, basemap, point_data):
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(15, 15))
    
        # Plot the basemap
        basemap.plot(ax=ax, color='white', edgecolor='black')
    
        # Plot the point data on top of the basemap
        point_data.plot(ax=ax, marker='o', color='blue', markersize=1)
    
        # Show the combined plot
        plt.show()



    

    

    
        
        