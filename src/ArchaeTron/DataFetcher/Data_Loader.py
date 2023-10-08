import geopandas as gpd
import pandas as pd
# class to load local data from files and databases

class DataLoader:
    def __init__(self):
        self.data_file = None
        self.data_dir = None
        self.data_db = None
        self.territory_type = None

  
    def load_csv(self, csv_file):
        # Load data from file
        try:
            # Use pandas to read the csv file
            df = pd.read_csv(csv_file)

            # Print information about the loaded csv file (optional)
            print(f"CSV file loaded from {csv_file}.")
            print(f"Number of rows: {len(df)}")
            print(f"Columns: {df.columns}")
            print(f"Data types: {df.dtypes}")
            print(f"Head: {df.head()}")

            return df

        except Exception as e:
            print(f"Error occurred while loading the csv file: {e}")
            return None


        

    def load_data_dir(self, data_dir):
        # Load data from directory
        pass

    def load_data_db(self, data_db):
        # Load data from database
        pass    



    # Load point data from local shapefile

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
        


    #Load polygon data from local shapefile

    def load_polygon_shapefile(self, shapefile_path):
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
    

        
