import geopandas as gpd
# class to load local data from files and databases

class DataLoader:
    def __init__(self):
        self.data = None
        self.data_file = None
        self.data_dir = None
        self.data_db = None
        self.shapefile_path = None
        self.territory_type = None

  
    def load_data(self, data_file):
        # Load data from file
        pass

    def load_data_dir(self, data_dir):
        # Load data from directory
        pass

    def load_data_db(self, data_db):
        # Load data from database
        pass    

    def load_point_shapefile(self, shapefile_path):
        # Fetch point data from local shapefile
        try:
            # Use geopandas to read the shapefile
            gdf = gpd.read_file(shapefile_path)

            # Print information about the loaded shapefile (optional)
            print(f"Shapefile loaded from {shapefile_path}.")
            print(f"Number of rows: {len(gdf)}")
            print(f"Columns: {gdf.columns}")
            print(f"CRS: {gdf.crs}")

            return gdf
    
        except Exception as e:
            print(f"Error occurred while loading the shapefile: {e}")
            return None
        
    
    def load_polygon_shapefile(self, shapefile_path):
        gdf = gpd.read_file(self.shapefile_path)

        # Print information about the loaded shapefile (optional)  
        print(f"Shapefile loaded from {self.shapefile_path}.")
        print(f"Number of rows: {len(gdf)}")
        print(f"Columns: {gdf.columns}")
        print(f"CRS: {gdf.crs}")

        
        return gdf
    

        # Fetch polygon data from local shapefile

        
