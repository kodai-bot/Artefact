

from Factories.Archae_Object_Factory import *
from DataFetcher.API_Methods import *
from WebInterface import *
import gradio as gr
from GeoDataHandler.GeopandasHandler import *



def main():
  
   # Acquire data
   # Create a test geopandas handler
   geopandas_handler = GeopandasHandler()
   # Load geospatial data


   # fetch data from logainm.ie api 
   api_url_placenames = "https://www.logainm.ie/api/v1.0/administrative-units/"  # Replace this with the actual API URL
   api_key = "VHjGfxN2wrKL88viNCn378nCHX2eXS"
    # params = {
       # "county": "YourTargetCounty",
       # "other_parameters": "other_values",
    #}
   data = fetch_data_from_api(api_url_placenames, api_key)
   # parsed_file = parse_json(data)


   for item in data["results"]:
       print(item)
   
   

   
   # Create concrete archaeological object factories

   sensed_factory = ConcreteSensedFactory()
   inferred_factory = ConcreteInferredFactory()

   # Create Archaeological Objects of either class using the factory
   name1 = "Rath"
   name2 = "Standing Stone"
   sensed_object = sensed_factory.create_sensed(name1)
   inferred_object = inferred_factory.create_inferred(name2)

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
)
    
   demo.launch()





if __name__ == "__main__":
   main()