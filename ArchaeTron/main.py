

from Factories.Archae_Object_Factory import *
from Builders.ObjectBuilder import *
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
   name1 = "Lios an Doill" # Data from API goes here
   name2 = "Rath"          # Iterator for object creation goes here

   # Obsolete code
   # sensed_object = sensed_factory.create_sensed(name1)
   # inferred_object = inferred_factory.create_inferred(name2)
   

   # Create builders for Archaeological Objects
   sensed_builder = sensed_factory.create_sensed_builder()
   inferred_builder = inferred_factory.create_inferred_builder()

   # Build Archaeological Objects using the builders
   # Build Sensed Object
   sensed_builder.set_data(name1)
   sensed_object = sensed_builder.build()

   sensed_obj = sensed_object.__repr__
   inf_result = "Inference result"

   # Build Inferred Object
   inferred_builder.set_inference_result(name2)
   inferred_builder
   inferred_builder.add_sensed_object(sensed_object)
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
)
    
   demo.launch()





if __name__ == "__main__":
   main()