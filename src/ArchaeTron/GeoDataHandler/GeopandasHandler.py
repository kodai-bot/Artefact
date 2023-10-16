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
    
    def return_polygon_centroid(self, polygon):
        # Return polygon centroid
        polygon_centroid = polygon.centroid
        return polygon_centroid
    
   

    def merge_and_rename_polygons(geodataframe, index1, index2, new_polygon_name):
        # Select the two rows (polygons) by their indices
        polygon1 = geodataframe.iloc[[index1]]
        polygon2 = geodataframe.iloc[[index2]]

        # Concatenate (merge) the selected polygons into a single new polygon
        merged_polygon = gpd.GeoDataFrame(pd.concat([polygon1, polygon2], ignore_index=True))

        # Set the new polygon's name (the "new_polygon_name" argument)
        merged_polygon['new_name'] = new_polygon_name

        # Append the merged polygon to the original GeoDataFrame
        result_geodataframe = geodataframe.append(merged_polygon, ignore_index=True)

        return result_geodataframe

        # Example usage:
        # Assuming you have a GeoDataFrame named 'gdf' and you want to merge rows at indices 1 and 2 into a new polygon with the name 'MergedPolygon'
        # result_gdf = merge_and_rename_polygons(gdf, 1, 2, 'MergedPolygon')
