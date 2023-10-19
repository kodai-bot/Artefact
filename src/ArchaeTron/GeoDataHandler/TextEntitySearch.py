import spacy
import geopandas as gpd
import re
# nlp = spacy.load("en_core_web_sm")



# class to recover measurements and shapes from text in a column of a geodataframe.

class TextProcessor:
    def __init__(self, gdf, text_column):
        self.gdf = gdf
        self.text_column = text_column
        self.measurement_pattern = r'\d+(\.\d+)?\s*(meters?|metres?|m|mm|cm)'
        self.shape_pattern = r'(circular|square)'
        

    
    def create_columns(self):
        if self.text_column not in self.gdf.columns:
            print(f"'{self.text_column}' column not found in the data.")
            

        self.gdf['Shape'] = None
        self.gdf['Measurements'] = None

    

    def process_text(self):
        for index, row in self.gdf.iterrows():
            text = row['self.text_column']

            # Search for shape words
            shape_match = re.search(self.shape_pattern, text)
            if shape_match:
                self.gdf.loc[index, 'Shape'] = shape_match.group(0)

            # Search for measurements
            measurement_match = re.search(self.measurement_pattern, text)
            if measurement_match:
                self.gdf.loc[index, 'Measurements'] = measurement_match.group(0)

        return self.gdf



        def save_data(self, path):
            self.data.to_csv(path, index=False)
            print(f"Data saved to {path}.")

        



