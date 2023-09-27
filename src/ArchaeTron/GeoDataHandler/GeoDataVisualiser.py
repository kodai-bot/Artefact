import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import 


class GeoDataVisualiser:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        fig, ax = plt.subplots(figsize=(15, 15))
        self.data.plot(ax=ax)
        plt.show()
        
        