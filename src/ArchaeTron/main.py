

from Factories.Archae_Object_Factory import *
from Builders.ObjectBuilder import *
from DataFetcher.APIHandler import *
from WebInterface import *
import gradio as gr
from GeoDataHandler.GeopandasHandler import *
from DataFetcher.Data_Loader import DataLoader
import geopandas as gpd
from GeoDataHandler.GeoDataVisualiser import GeoDataVisualiser
from GeoDataHandler.TextEntitySearch import TextProcessor  # This is the class that will be used to process the text data
import sys
from DataFetcher.APIHandler import JSONHandler
import threading





def main():
   
   
    # Acquire monuments point data from local file. This is ALL known monuments in Ireland.
    # Uses a DataLoader class to load the data

    
    #monuments_loader = DataLoader()
    #monuments_zip = "zip:///Users/mensab/Documents/GISMapFiles/NMS_OpenData_20230623_shp.zip"
    #monuments_map = monuments_loader.load_point_shapefile(monuments_zip)
   

    # Load geospatial data from local shapefiles. These are downloaded from the OSI website
    # Uses a DataLoader class to load the data

    # Load baronies shapefile
    baronies_loader = DataLoader()
    barony_zip = "zip:///Users/mensab/Documents/GISMapFiles/Baronies_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    barony_map = baronies_loader.load_polygon_shapefile(barony_zip)

    # Load provinces shapefile
    provinces_loader = DataLoader()
    province_zip = "zip:///Users/mensab/Documents/GISMapFiles/Provinces_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    province_map = provinces_loader.load_polygon_shapefile(province_zip)

    # Load civil parishes shapefile
    civil_parishes_loader = DataLoader()
    civil_parish_zip = "zip:///Users/mensab/Documents/GISMapFiles/Civil_Parishes_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    civil_parish_map = civil_parishes_loader.load_polygon_shapefile(civil_parish_zip)

    # Load townlands shapefile
    #townlands_loader = DataLoader()
    #townland_zip = "zip:///Users/mensab/Documents/GISMapFiles/Townlands_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    #townland_map = townlands_loader.load_polygon_shapefile(townland_zip)

    # Load counties shapefile
    counties_loader = DataLoader()
    county_zip = "zip:///Users/mensab/Documents/GISMapFiles/Counties_-_National_Statutory_Boundaries_-_2019_-_Generalised_20m.zip"
    county_map = counties_loader.load_polygon_shapefile(county_zip)

    # Load TII (Transport Infrastructure Ireland) Archaeology shapefile

    #tii_loader = DataLoader()
    #tii_zip = "zip:////Users/mensab/Documents/GISMapFiles/TIIArchaeology.zip"
    #tii_map = tii_loader.load_point_shapefile(tii_zip)

    # Connect to the API and fetch data
    # Connect to available api  Monuments services are offline
    # Monuments API is below, the data has been loaded above as a file while API is offline.

    # api_url_monuments = "https://webservices.archaeology.ie/arcgis/rest/services/NM/NationalMonuments/MapServer"  # Monuments API

    # Folklore API
    # API key is obtained from GAOIS (https://www.duchas.ie/en/info/api)
    
    api_key = "vV6BzMTwGGIBbOFF6lASOir1qWQ1Jh"
    schools_folklore_loader = APIHandler()
    api_url_folklore = "https://www.duchas.ie/api/v0.6/cbes"  # Folklore API
    schools_topics_list = schools_folklore_loader.fetch_data_from_api(api_url_folklore, api_key)
    print(schools_topics_list)





    # Connect to Logainm API and fetch data
    placenames_loader = APIHandler()
    api_handshake = placenames_loader.fetch_data_from_api("https://www.logainm.ie/api/v1.0/", api_key)
    api_url_admin_units = "https://www.logainm.ie/api/v1.0/administrative-units/"
    api_url_lat_long = "https://www.logainm.ie/api/v1.0/?Latitude=54.26969&Longitude=-8.46943&Radius=3000"

  
    # params = {
        # "county": "YourTargetCounty",
        # "other_parameters": "other_values",
     #}

    admin_units_data = placenames_loader.fetch_data_from_api(api_url_admin_units, api_key)
    lat_long_data = placenames_loader.fetch_data_from_api(api_url_lat_long, api_key)

    print(admin_units_data)
    print("potato")
    print(json.dumps(lat_long_data, indent=4, sort_keys=True))

    

    # Save the data to a local file
    json_handler = JSONHandler()
    #json_handler.save_data_to_file(admin_units_data, 'admin_units_data.json')
    json_handler.save_data_to_file(lat_long_data, 'lat_long_data.json')


    sys.exit()


    #parsed_file = parse_json(data)
    #for item in data["results"]:
        #print(item)




    # Save the data to a local file



    # _______________________________________________________________________________________________________________________

    # Initial data visualisation of full dataset

    #visualiser = GeoDataVisualiser()
    #visualiser.plot_data(barony_map)
  

    # Visualise the data for the northwest counties

    northwest_monuments = monuments_map[monuments_map['COUNTY'].isin(['SLIGO', 'DONEGAL','LEITRIM'])]
    # visualiser.plot_data_combined(barony_map, monuments_map)
   








    # _______________________________________________________________________________________________________________________
   
    # Feature engineering
    # Take an existing GeoDataFrame
    #existing_gdf = gpd.read_file('your_shapefile.shp')  # Replace with your shapefile

    # Extract the columns you want
    #column1_values = existing_gdf['column1']
    #column2_values = existing_gdf['column2']



    
    # Create a test geopandas handler
    geopandas_handler = GeopandasHandler()

    
    # Define the mapping dictionary to use for value replacement. This is a dictionary of key-value pairs

    #replacement_map = {
    #'Rath': 'Radial',
    #'': 'SomeValue',  # Add more mappings as needed
#}

    # Use the function to replace values
    gdf =  replace_values(gdf, source_column='M_Type', target_column='Symmetry', mapping_dict=replacement_map)







    # _______________________________________________________________________________________________________________________
   
    # Create concrete archaeological object factoriesm these will create builders for the objects
    # and the GeoDataFrame builder will assemble them into a GeoDataFrame

    # Sensed Object Factory
    sensed_factory = ConcreteSensedFactory()

    # Inferred Object Factory
    inferred_factory = ConcreteInferredFactory()

    # Concrete GeoDataFrame factory
    geodataframe_factory = ConcreteGeoDataFrameFactory()

    
    
    # Create builders for Archaeological Objects

    # Sensed Object Builder
    sensed_builder = sensed_factory.create_sensed_builder()
    
    # Inferred Object Builder
    inferred_builder = inferred_factory.create_inferred_builder()

    # Create a concrete GeoDataFrame builder
    geodataframe_builder = geodataframe_factory.create_GeoDataFrameBuilder()


    # _______________________________________________________________________________________________________________________

    # Create Archaeological Objects of either class using the builders

    name1 = "Lios an Doill" # Data from API goes here
    name2 = "Rath"          # Iterator for object creation goes here

    #  Obsolete code
    # sensed_object = sensed_factory.create_sensed(name1)
    # inferred_object = inferred_factory.create_inferred(name2)
   

    

    # Build Archaeological Objects using the builders


    # Build Sensed Objects
    sensed_builder.set_data("Sensed data")
    sensed_builder.set_name(name1)
    sensed_builder.set_sensed_position(35, 45, 55)
    sensed_builder.set_incept_position(1250)
    sensed_builder.set_destruct_position(300)
     

   
    sensed_object = sensed_builder.build()

    sensed_obj = sensed_object.__repr__
    inf_result = "Inference result"

    # Build Inferred Objects
    inferred_builder.set_inference_result(name2)
    inferred_builder.add_sensed_object(sensed_obj)
    inferred_builder.add_name(name = "potato")
    inferred_object = inferred_builder.build()


    # view objects structure

    print(sensed_object.__dict__)
    print(inferred_object.__dict__)
    print(sensed_object.__class__)
    print(inferred_object.__class__)
    print(sensed_object.__repr__)
    print(inferred_object.__repr__)
    print(sensed_object.name)


    # _______________________________________________________________________________________________________________________


    # Feature engineering

    # Create a text processor to extract measurement and shape data.

    
    processor = TextProcessor(northwest_monuments, 'WEB_NOTES')
    processor.create_columns()
    northwest_monuments = processor.process_text()
    print(northwest_monuments.head())
    #northwest_monuments.to_csv('northwest_monuments.csv', index=False)






    # Convert the objects to a GeoDataFrame

    # Encode columns as categorical data
    


# _______________________________________________________________________________________________________________________

    # Choose machine learning model to use for inference


    # Evaluate the model


    # Save the model


# _______________________________________________________________________________________________________________________
    # Display the results 
    
    # Create a test web interface

    def greet(name):
        return "Hello " + name + "!"
   
   
    demo = gr.Interface(
     fn=greet,
     inputs=gr.Textbox(lines=2, placeholder="potato", label="Name"),
     outputs="text",
     title="Greeting",)
    
    demo.launch()





if __name__ == "__main__":
    main()