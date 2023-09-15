import geopandas as gpd
from shapely.geometry import Point

class GeopandasHandler:
    def __init__(self):
        # Initialize Geopandas settings
    
    def load_geospatial_data(self, file_path):
        # Load geographic data using Geopandas
    
    def visualize_data(self, data):
        # Create maps and visualizations

    def create_buffer(self, data):
        # Create buffer zones around geographic data
        # Create a buffer around the polygon edges (adjust the buffer distance as needed)
        buffer_distance = 0.001  # This is in the same units as your shapefiles (e.g., meters or degrees)
        polygons['geometry'] = polygons['geometry'].buffer(buffer_distance)

        # Check if points are within the polygon buffer
        points_within_buffer = gpd.sjoin(points, polygons, op='within')
        return points_within_buffer