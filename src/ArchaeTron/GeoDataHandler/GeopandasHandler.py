import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt


class GeopandasHandler:
    def __init__(self):
        # Initialize Geopandas settings
        pass
    
    def load_geospatial_data(self, file_path):
        df = gpd.read_file(file_path)
        return df
        # Load geographic data using Geopandas


    
    def visualize_data(self, data):
        # Visualize geographic data using Geopandas
        data.plot()
        plt.show()





        # Polygon data manipulation functions

    def create_polygon_buffer(self, polygon, buffer_distance):
        # Create polygon buffer
        polygon_buffer = polygon.buffer(buffer_distance)
        return polygon_buffer
    
    def return_points_within_buffer(self, polygon_buffer, points):
        # Return points within buffer
        points_within_buffer = points.within(polygon_buffer)
        return points_within_buffer
    
    def return_points_within_polygon(self, polygon, points):
        # Return points within polygon
        points_within_polygon = points.within(polygon)
        return points_within_polygon
    
    def merge_polygons(self, polygon1, polygon2):
        # Merge polygons
        merged_polygons = polygon1.union(polygon2)
        return merged_polygons