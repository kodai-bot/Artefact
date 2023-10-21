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

