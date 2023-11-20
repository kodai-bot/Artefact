import geopandas as gpd
from shapely.geometry import Point

# Query and return data at a specific point in a polygon or surface data structure.

class Query_Data_At_Location:
    def __init__(self, data_path):
        self.data_path = gpd.read_file(data_path)

    def get_data_type(self, longitude, latitude):
    # Create a Point object from the coordinates
    
        point = Point(longitude, latitude)

    # Check if the point is within any of the polygons in the soil data

        for index, row in self.data_path.iterrows():
            if point.within(row['geometry']):
                return row['data_type']

        # If no match is found, return None or a default value
        return None
