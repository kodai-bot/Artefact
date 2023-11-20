

from Factories.Archae_Object_Factory import *
from Builders.ObjectBuilder import *
from DataFetcher.APIHandler import *
from WebInterface import *
import gradio as gr
from GeoDataHandler.GeopandasHandler import *
from FileManager.Data_Loader import DataLoader
import geopandas as gpd
from GeoDataHandler.GeoDataVisualiser import GeoDataVisualiser
from GeoDataHandler.TextEntitySearch import TextProcessor  # This is the class that will be used to process the text data
import sys
from DataFetcher.APIHandler import JSONHandler
import threading
from FileManager.data_saver import DataSaver
from TimeHandler.StateVectors import StateVector






def main():
   
   
    # Acquire monuments point data from local file. This is ALL known monuments in Ireland.
    # Uses a DataLoader class to load the data
    # DATA FROM LOCAL FILES

    
    monuments_loader = DataLoader()
    #monuments_zip = "zip:///Users/mensab/Documents/GISMapFiles/NMS_OpenData_20230623_shp.zip"
    #monuments_map = monuments_loader.load_point_shapefile(monuments_zip)

    # Load monuments data from local file. This data has been cleaned and filtered to only include monuments in the northwest counties. 

    nw_monuments = monuments_loader.load_point_shapefile("/Users/mensab/Documents/GISMapFiles/NorthWestMonuments.shp")

    #monuments_copy = monuments_map.copy() 
    filesaver = DataSaver()
    #filesaver.save_gdf_to_shapefile(monuments_copy, "monuments.shp")
    

    # Load geospatial data from local shapefiles. These are downloaded from the OSI website
    # Uses a DataLoader class to load the data

    # Load baronies shapefile
    #baronies_loader = DataLoader()
    #barony_zip = "zip:///Users/mensab/Documents/GISMapFiles/#Baronies_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    #barony_map = baronies_loader.load_polygon_shapefile(barony_zip)

    # Load provinces shapefile
    # provinces_loader = DataLoader()
    # province_zip = "zip:///Users/mensab/Documents/GISMapFiles/#Provinces_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    # province_map = provinces_loader.load_polygon_shapefile(province_zip)

    # Load civil parishes shapefile
    #civil_parishes_loader = DataLoader()
    #civil_parish_zip = "zip:///Users/mensab/Documents/GISMapFiles/#Civil_Parishes_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    #civil_parish_map = civil_parishes_loader.load_polygon_shapefile(civil_parish_zip)

    # Load townlands shapefile
    #townlands_loader = DataLoader()
    #townland_zip = "zip:///Users/mensab/Documents/GISMapFiles/#Townlands_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    #townland_map = townlands_loader.load_polygon_shapefile(townland_zip)

    # Load counties shapefile
    #counties_loader = DataLoader()
    #county_zip = "zip:///Users/mensab/Documents/GISMapFiles/#Counties_-_National_Statutory_Boundaries_-_2019_-_Generalised_20m.zip"
    #county_map = counties_loader.load_polygon_shapefile(county_zip)


    # Excavations data

    # Load TII (Transport Infrastructure Ireland) Archaeology shapefile

    #tii_loader = DataLoader()
    #tii_zip = "zip:////Users/mensab/Documents/GISMapFiles/TIIArchaeology.zip"
    #tii_map = tii_loader.load_point_shapefile(tii_zip)

    # Excavations.ie data



    # Geographic features data

    #Load ground cover data from local file
    #ground_cover_loader = DataLoader()
    #ground_cover = "/Users/mensab/Documents/GISMapFiles/CLC18_IE_ITM"
    #ground_cover_map = ground_cover_loader.load_polygon_shapefile(ground_cover)

    # Load rivers data from local file
    #rivers_loader = DataLoader()
    #rivers = "/Users/mensab/Documents/GISMapFiles/Rivers&Lakes/Shapefiles"
    #rivers_map = rivers_loader.load_polygon_shapefile(rivers)

    # Load soils data from local file
    #soils_loader = DataLoader()
    #soils = "/Users/mensab/Documents/GISMapFiles/SOIL_SISNationalSoils_shp/Data/SOIL_SISNationalSoils_Shp"
    #soils_map = soils_loader.load_polygon_shapefile(soils)

    # Load height data from local file
    #heights_loader = DataLoader()
    #heights = "/Users/mensab/Documents/GISMapFiles/srtm_35_02/srtm_35_02.tif"
    #heights_map = heights_loader.load_raster(heights)




    # API DATA

    # Connect to the API and fetch data
    # API calls are made using the APIHandler class

    # api_url_monuments = "https://webservices.archaeology.ie/arcgis/rest/services/NM/NationalMonuments/MapServer"  # Monuments API

    # Folklore API at logainm.ie
    # API key is obtained from GAOIS (https://www.duchas.ie/en/info/api)
    
    api_key = "vV6BzMTwGGIBbOFF6lASOir1qWQ1Jh"

    #schools_folklore_loader = APIHandler()
    #api_url_folklore = "https://www.duchas.ie/api/v0.6/cbes"  # Folklore API
    #schools_topics_list = schools_folklore_loader.fetch_data_from_api(api_url_folklore, api_key)
    #print(schools_topics_list)

    # Connect to Logainm API and fetch data
    #placenames_loader = APIHandler()
    #api_handshake = placenames_loader.fetch_data_from_api("https://www.logainm.ie/api/v1.0/", api_key)
    
    # API address for administrative units

    api_url_admin_units = "https://www.logainm.ie/api/v1.0/administrative-units/"
    api_url_lat_long = "https://www.logainm.ie/api/v1.0/?Latitude=54.26969&Longitude=-8.46943&Radius=3000"

    # params = {
        # "county": "YourTargetCounty",
        # "other_parameters": "other_values",
     #}
    
    # Test API calls
    #admin_units_data = placenames_loader.fetch_data_from_api(api_url_admin_units, api_key)
    #lat_long_data = placenames_loader.fetch_data_from_api(api_url_lat_long, api_key)

    #print(admin_units_data)
    #print("potato")
    #print(json.dumps(lat_long_data, indent=4, sort_keys=True))

    # Save returned data to a local file
    #json_handler = JSONHandler()
    #json_handler.save_data_to_file(admin_units_data, 'admin_units_data.json')
    #json_handler.save_data_to_file(lat_long_data, 'lat_long_data.json')


 
    
    # PDF Extraction
    # Onomastiocon Goedilicum

    # Load the PDF file
    #pdf_handler = PDFHandler()
    #pdf_file = pdf_handler.load_pdf_file("/Users/mensab/Documents/GISMapFiles/Onomasticon_Goedilicum.pdf")

    # Data scraping
    # EDIL (Electronic Dictionary of the Irish Language)
    # https://edil.qub.ac.uk/
    # Named entity recognition

    # Wikipedia 
    # https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Donegal&format=json
    
    # API call to Wikipedia
    wikipedia_loader = APIHandler()
    api_url_wikipedia = "https://en.wikipedia.org/w/api.php"
    wikipedia_data = wikipedia_loader.fetch_data_from_wikipedia_api(api_url_wikipedia, api_key, "Cairbre Drom Cliabh")
    print(wikipedia_data)

    # Save returned data to a local file
    json_handler = JSONHandler()
    json_handler.save_data_to_file(wikipedia_data, 'wikipedia_data.json')
    

    




    





    #parsed_file = parse_json(data)
    #for item in data["results"]:
        #print(item)

    #print(data["results"][0]["county"])

    # Save the data to a local file



    # _______________________________________________________________________________________________________________________
    # Create object for gdf preprocessing
    gdf_processor = GeopandasHandler()

    # Convert the crs to epsg:4326 Standard WGS84 projection, used in GeoJSON and Google Earth
    # Also important for web mapping, and for feature engineering distances and areas on a curved surface.
    #target_epsg = 4326
    #monuments_map = gdf_processor.change_crs(target_epsg, monuments_map)
    #barony_map = gdf_processor.change_crs(target_epsg, barony_map)
    #province_map = gdf_processor.change_crs(target_epsg, province_map)
    #civil_parish_map = gdf_processor.change_crs(target_epsg, civil_parish_map)
    ##townland_map = gdf_processor.change_crs(target_epsg, townland_map)
    #county_map = gdf_processor.change_crs(target_epsg, county_map)

    # Select the monument data for the northwest counties

    northwest_monuments = monuments_copy[monuments_map['COUNTY'].isin(['SLIGO', 'DONEGAL','LEITRIM'])]
    print(northwest_monuments.head())
    print(northwest_monuments.shape())


    # Create the state vectors for the data objects. 
    # These allow the different states at different times to be accessed. 

    from TimeHandler.positionCalculator import to_equatorial

    # Get equatorial coordinates for the objects in this study area.
    Map_Lat, Map_Long = 54.26969, -8.46943
    Map_RA, Map_Dec = to_equatorial(Map_Lat, Map_Long)
    


    Barony_Map_Vector = StateVector()
    # t=0 is the present day map, each step in t is a change in object state.

    Barony_Map_Vector.add_state(t=0, ra=Map_RA, dec=Map_Dec, z_0=0, object_details=baronies_NW, inception_point= None)
    Barony_Map_Vector.add_state(t=1, ra=Map_RA, dec=Map_Dec, z_0=423, object_details=baronies_NW_1600, inception_point= None)

    Monuments_Map_Vector = StateVector()
    Monuments_Map_Vector.add_state(t=0, ra=10, dec=20, z_0=23, object_details=monuments_NW_clean, inception_point= None)
    Monuments_Map_Vector.add_state(t=1, ra=10, dec=20, z_0=423, object_details=monuments_NW_1600, inception_point= None)





    timestep = 0  # Choose a specific time step
    state_timestep = BaronyMap.get_state(timestep)

    # Extracting information from the state vector
    # Extracting information from the state vector
    x_coord = state_timestep['RA']
    y_coord = state_timestep['Dec']
    z_coord = state_timestep['z_0']
    object_details = state_timestep['object_details']

    
    


    

    # Visualise the data for the northwest counties

    #print(barony_map.crs)
    #print(province_map.crs)
    #print(civil_parish_map.crs)
    #print(townland_map.crs)
    #print(county_map.crs)
    print(monuments_copy.crs)

    #visualiser = GeoDataVisualiser()
    #visualiser.plot_data(barony_map)
    #visualiser.plot_data(province_map)
    #visualiser.plot_data(civil_parish_map)
  

    sys.exit()

    # visualiser.plot_data_combined(barony_map, monuments_map)


   
    # Save modified data to a local file







    # _______________________________________________________________________________________________________________________
   
    # Feature engineering
    # Take an existing GeoDataFrame
    #existing_gdf = gpd.read_file('your_shapefile.shp')  # Replace with your shapefile

    # Extract the columns you want
    #column1_values = existing_gdf['column1']
    #column2_values = existing_gdf['column2']

# Example usage of the Fetch_Location Data object
   # soil_analyzer = SoilTypeAnalyzer('path/to/your/soil_data.shp')
   #longitude = 25.0
   # latitude = 40.0
   # soil_type = soil_analyzer.get_soil_type(longitude, latitude)
   #if soil_type:
   #     print(f"The soil type at ({longitude}, {latitude}) is: {soil_type}")
  # else:

    
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


    # Example usage:
    # archaeo_objects = create_archaeo_objects_from_geodataframe(your_geodataframe_variable)


    # Example usage:
    # original_geodataframe = your_original_geodataframe_variable
    # archaeo_objects = create_archaeo_objects_from_geodataframe(original_geodataframe)

    # Modify attributes of the ArchaeoObjects using the builder pattern
    for obj in archaeo_objects:
        obj.set_number(5).set_classname('NewClass').set_latitude(53.349805).set_longitude(-6.26031)

    # Update attributes as needed

    # Convert the list of ArchaeoObjects back to a new GeoDataFrame
    # new_geodataframe = convert_to_geodataframe(archaeo_objects, original_geodataframe)



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