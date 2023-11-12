import geopandas as gpd
import pandas as pd
import threading
import rasterio as rio

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


    def load_data_concurrently(self, file_paths):
        # Load data from multiple files concurrently using threads
        threads = []

        for file_path in file_paths:
            if file_path.endswith('.csv'):
                thread = threading.Thread(target=self.load_csv, args=(file_path,))
            elif file_path.endswith('.shp'):
                thread = threading.Thread(target=self.load_point_shapefile, args=(file_path,))
            elif file_path.endswith('.dbf'):
                thread = threading.Thread(target=self.load_polygon_shapefile, args=(file_path,))
            elif file_path.endswith('.json'):
                thread = threading.Thread(target=self.load_json, args=(file_path,))
            elif file_path.endswith('.geojson'):
                thread = threading.Thread(target=self.load_geojson, args=(file_path,))
            else:
                # Handle other file types or raise an error if needed
                pass

            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()
    
    
    def load_json(self, json_file):
        # Load data from file
        try:
            # Use pandas to read the csv file
            df = pd.read_json(json_file)

            # Print information about the loaded csv file (optional)
            print(f"JSON file loaded from {json_file}.")
            print(f"Number of rows: {len(df)}")
            print(f"Columns: {df.columns}")
            print(f"Data types: {df.dtypes}")
            print(f"Head: {df.head()}")

            return df

        except Exception as e:
            print(f"Error occurred while loading the json file: {e}")
            return None
        

    def load_geojson(self, geojson_file):
        # Load data from file
        try:
            # Use pandas to read the csv file
            gdf = gpd.read_json(geojson_file)

            # Print information about the loaded csv file (optional)
            print(f"JSON file loaded from {geojson_file}.")
            print(f"Number of rows: {len(df)}")
            print(f"Columns: {df.columns}")
            print(f"Data types: {df.dtypes}")
            print(f"Head: {df.head()}")

            return df

        except Exception as e:
            print(f"Error occurred while loading the geojson file: {e}")
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
    

        # Load suface data from local raster file
    def load_raster(self, raster_file):
        try:
            # Use rasterio to read the raster file
            raster = rio.open(raster_file)

            # Print information about the loaded raster file (optional)
            print(f"Raster file loaded from {raster_file}.")
            print(f"Number of bands: {raster.count}")
            print(f"Width: {raster.width}")
            print(f"Height: {raster.height}")
            print(f"CRS: {raster.crs}")
            print(f"Bounds: {raster.bounds}")

            return raster
        
        except Exception as e:
            print(f"Error occurred while loading the raster file: {e}")
            return None
        
        
