import json  
import geopandas as gpd
import os


class DataSaver:

    def save_data_to_json_file(data, filename):
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Data saved to {filename} successfully.")
        except Exception as e:
            print(f"Error occurred while saving data: {e}")


    def save_data_to_csv_file(data, filename):
        with open(filename, "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)




    def save_data_to_shapefile(data, filename):

        # Save the GeoDataFrame to a Shapefile
        geopandas_dataframe.to_file(output_file, driver="ESRI Shapefile")

        # Check if the file was saved successfully
        if os.path.exists(output_file):
            print(f"Data saved to {output_file} successfully.")
            return True
        else:
            print("Error occurred while saving data.")
            return False
        


    # Save the GeoDataFrame to a GeoPackage file  

    def save_data_to_geopackage(data, filename):
        gpd.to_file(filename, driver="GPKG")

        # Check if the file was saved successfully

        if os.path.exists(filename):
            print(f"Data saved to {filename} successfully.")
            return True
        else:
            print("Error occurred while saving data.")
            return False
    


    def save_gdf_to_shapefile(geopandas_dataframe, output_file):
        """
        Save a GeoPandas DataFrame to a Shapefile.

        Args:
            geopandas_dataframe (geopandas.GeoDataFrame): The GeoPandas DataFrame to save.
            output_file (str): The file path where the Shapefile should be saved.
        
        Returns:
            bool: True if the data was saved successfully, False otherwise.
        """
        try:
            # Save the GeoDataFrame to a Shapefile
            geopandas_dataframe.to_file(output_file, driver="ESRI Shapefile")

            # Check if the file was saved successfully
            if os.path.exists(output_file):
                print(f"Data saved to {output_file} successfully.")
                return True
            else:
                print("Error occurred while saving data.")
                return False
        except Exception as e:
            print(f"Error occurred while saving data: {e}")
            return False


    def save_geopandas_to_geopackage(geopandas_dataframe, output_file):
        """
        Save a GeoPandas DataFrame to a GeoPackage file.

        Args:
            geopandas_dataframe (geopandas.GeoDataFrame): The GeoPandas DataFrame to save.
            output_file (str): The file path where the GeoPackage should be saved.
        
        Returns:
             bool: True if the data was saved successfully, False otherwise.
        """
        try:
            # Save the GeoDataFrame to a GeoPackage file
            geopandas_dataframe.to_file(output_file, driver="GPKG")

            # Check if the file was saved successfully
            if os.path.exists(output_file):
                print(f"Data saved to {output_file} successfully.")
                return True
            else:
                print("Error occurred while saving data.")
                return False
        except Exception as e:
            print(f"Error occurred while saving data: {e}")
            return False

    # Example usage:
    # Assuming you have a GeoPandas DataFrame named 'gdf' with your geospatial data
    # Specify the file path where you want to save the GeoPackage
    # output_file = "your_data.gpkg"

    # Call the function to save the GeoDataFrame
    # save_geopandas_to_geopackage(gdf, output_file)

