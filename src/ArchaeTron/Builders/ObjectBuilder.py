from Archae_Objects.ArchaeObj_Base_Class import *


class ArchObjectBuilder:
    def __init__(self):
        self.data = None
        self.name = None

    def set_data(self, data):
        self.data = data

    def set_name(self, name):
        self.name = name

    def set_sensed_position(self, sensed_position):
        self.sensed_position = sensed_position

    def set_incept_position(self, incept_position):
        self.incept_position = incept_position

    def set_destruction_position(self, destruct_position):
        self.destruction_position = destruct_position

    def build(self):
        return ArchObject(self.data, self.name, self.sensed_position, self.incept_position, self.destruct_position)
    


    class GeoDataFrameBuilder:
        def __init__(self, crs=None):
            self.data = {}      # Dictionary to store attribute data
            self.geometry = []  # List to store geometry objects
            self.crs = crs


        def add_data(self, column_name, values):
            self.data[column_name] = values
            return self  # Return the builder instance to allow method chaining
            

        def add_geometry(self, geometry):
            self.geometry.append(geometry)
            return self  # Return the builder instance to allow method chaining
        
        
        def set_crs(self, crs):
            self.crs = crs
            return self
        
        
        def build(self):
            if not self.geometry:
                raise ValueError("No geometry objects added. Please add at least one geometry.")

            if self.crs:
                gdf = gpd.GeoDataFrame(self.data, geometry=self.geometry, crs=self.crs)
            else:
                gdf = gpd.GeoDataFrame(self.data, geometry=self.geometry)

            return gdf
        
        
        # Define a function to create custom archaeo objects from a GeoDataFrame.
        # The function takes a GeoDataFrame as input and returns a list of ArchaeoObject instances.
        # The function assumes that the GeoDataFrame has columns named 'number', 'classname', 'latitude', and
        #'longitude'. These will need to be changed to match the column names in your GeoDataFrame. Or modify the # function to pass these as arguments

        def create_archaeo_objects_from_geodataframe(geodataframe):
            archaeo_objects = []
            for index, row in geodataframe.iterrows():
                # Assuming 'number', 'classname', 'latitude', and 'longitude' are column names in the GeoDataFrame
                number = row['number']
                classname = row['classname']
                latitude = row['latitude']
                longitude = row['longitude']

                # Creating ArchaeoObject instances
                archaeo_obj = ArchaeoObject(number, classname, latitude, longitude)
                archaeo_objects.append(archaeo_obj)

            return archaeo_objects  
        

        
        # Function to convert list of ArchaeoObjects back to a GeoDataFrame, pass the archaeo_objects list and # # the original GeoDataFrame as arguments

        def convert_to_geodataframe(archaeo_objects, original_geodataframe):
            data = {
                'number': [obj.number for obj in archaeo_objects],
                'classname': [obj.classname for obj in archaeo_objects],
                'latitude': [obj.latitude for obj in archaeo_objects],
                'longitude': [obj.longitude for obj in archaeo_objects]
            }
    
        # Create a new GeoDataFrame from the data and original GeoDataFrame's geometry

            new_geodf = gpd.GeoDataFrame(data, geometry=original_geodataframe.geometry)
            return new_geodf

