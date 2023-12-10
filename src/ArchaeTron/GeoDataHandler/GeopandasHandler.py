import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt


# Defines a class to handle GeoDataFrames


class GeopandasHandler:
    def __init__(self):
        # Initialize Geopandas settings
        pass

     # Function to change the CRS of multiple GeoPandas DataFrames
    def change_crs(self, target_epsg, gdf):

        # Change the CRS of the GeoDataFrame
        gdf = gdf.to_crs(epsg=target_epsg)

        # Return the updated GeoDataFrame
        return gdf  
       
    

    # Define a function to apply value replacements based on a mapping dictionary
    def replace_values(df, source_column, target_column, mapping_dict):
        # df: The GeoDataFrame to operate on
        # source_column: The column to read values from
        # target_column: The column to write the replaced values to
        # mapping_dict: A dictionary mapping values in the source column to new values

        # Use the replace method to apply the replacements and store the result in the target column
        df[target_column] = df[source_column].replace(mapping_dict)

        # Return the updated GeoDataFrame
        return df
      
    # Define a function to create a GeoDataFrame from a list of coordinates
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
    
    
    # NOTE: Polygons must intersect for a union operation to work on them.

    def merge_polygons(self, polygon1, polygon2):
        # Merge polygons
        merged_polygons = polygon1.union(polygon2)
        return merged_polygons
    
    def return_polygon_centroid(self, polygon):
        # Return polygon centroid
        polygon_centroid = polygon.centroid
        return polygon_centroid
    
    def add_column_to_geodataframe(self, geodataframe, column_name, column_data):
        # Add column to GeoDataFrame
        geodataframe[column_name] = column_data
        return geodataframe


    
   # NOTE: Polygons must intersect for a union operation to work on them.

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
        # Assuming you have a GeoDataFrame named 'gdf' and you want to merge rows at indices 1 and 2 into a new
        # polygon with the name 'MergedPolygon'
        # result_gdf = merge_and_rename_polygons(gdf, 1, 2, 'MergedPolygon')






    
        print(f"No soil data found for the coordinates ({longitude}, {latitude}).")



        
