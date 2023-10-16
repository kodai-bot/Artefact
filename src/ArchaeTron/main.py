

from Factories.Archae_Object_Factory import *
from Builders.ObjectBuilder import *
from DataFetcher.APIHandler import *
from WebInterface import *
import gradio as gr
from GeoDataHandler.GeopandasHandler import *
from DataFetcher.Data_Loader import DataLoader
import geopandas as gpd
from GeoDataHandler.GeoDataVisualiser import GeoDataVisualiser





def main():
   
   
    # Acquire monuments point data from local file. This is ALL known monuments in Ireland.
    # Uses a DataLoader class to load the data

    monuments_loader = DataLoader()
    monuments_zip = "zip:///Users/mensab/Documents/GISMapFiles/NMS_OpenData_20230623_shp.zip"
    monuments_map = monuments_loader.load_point_shapefile(monuments_zip)
   

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
    townlands_loader = DataLoader()
    townland_zip = "zip:///Users/mensab/Documents/GISMapFiles/Townlands_-_OSi_National_Statutory_Boundaries_-_Generalised_20m-shp.zip"
    townland_map = townlands_loader.load_polygon_shapefile(townland_zip)

    # Load counties shapefile
    counties_loader = DataLoader()
    county_zip = "zip:///Users/mensab/Documents/GISMapFiles/Counties_-_National_Statutory_Boundaries_-_2019_-_Generalised_20m.zip"
    county_map = counties_loader.load_polygon_shapefile(county_zip)

    # Load TII (Transport Infrastructure Ireland) Archaeology shapefile

    tii_loader = DataLoader()
    tii_zip = "zip:////Users/mensab/Documents/GISMapFiles/TIIArchaeology.zip"
    tii_map = tii_loader.load_point_shapefile(tii_zip)

    # Connect to the API and fetch data
    # Connect to available api  Monuments services are offline
    # Monuments API is below, the data has been loaded above as a file while API is offline.

    # api_url_monuments = "https://webservices.archaeology.ie/arcgis/rest/services/NM/NationalMonuments/MapServer"  # Replace this with the actual API URL

    # Connect to Logainm API and fetch data
    placenames_loader = APIHandler()
    api_url_placenames = "https://www.logainm.ie/api/v1.0/administrative-units/"  # Replace this with the actual API URL
    api_key = "VHjGfxN2wrKL88viNCn378nCHX2eXS"
    # params = {
        # "county": "YourTargetCounty",
        # "other_parameters": "other_values",
     #}

    #placenames_data = placenames_loader.fetch_data_from_api(api_url_placenames, api_key)

    # parsed_file = parse_json(data)
    #for item in data["results"]:
        #print(item)


    # _______________________________________________________________________________________________________________________

    # Initial data visualisation

    visualiser = GeoDataVisualiser()
    visualiser.plot_data(barony_map)

    
    filtered_points = monuments_map[monuments_map['COUNTY'].isin(['SLIGO', 'DONEGAL'])]
    visualiser.plot_data_combined(barony_map, monuments_map)








    # _______________________________________________________________________________________________________________________
   
    # Create a test geopandas handler
   

    geopandas_handler = GeopandasHandler()






    # _______________________________________________________________________________________________________________________
   
    # Create concrete archaeological object factories

    sensed_factory = ConcreteSensedFactory()
   
    inferred_factory = ConcreteInferredFactory()

    # Create Archaeological Objects of either class using the factory
    name1 = "Lios an Doill" # Data from API goes here
    name2 = "Rath"          # Iterator for object creation goes here

    #  Obsolete code
    # sensed_object = sensed_factory.create_sensed(name1)
    # inferred_object = inferred_factory.create_inferred(name2)
   

    # Create builders for Archaeological Objects
    sensed_builder = sensed_factory.create_sensed_builder()
    inferred_builder = inferred_factory.create_inferred_builder()

    # Build Archaeological Objects using the builders
    # Build Sensed Object
    sensed_builder.set_data("Sensed data")
    sensed_builder.set_name(name1)
    sensed_builder.set_sensed_position(35, 45, 55)
    sensed_builder.set_incept_position(1250)
    sensed_builder.set_destruct_position(300)
     

   
    sensed_object = sensed_builder.build()

    sensed_obj = sensed_object.__repr__
    inf_result = "Inference result"

    # Build Inferred Object
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