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
    




class MotionTraceBuilder:
    def __init__(self):
        self.inference_result = None    
        self.sensed_objects = []
        self.name = None

    def set_inference_result(self, inference_result):
        self.inference_result = inference_result

    def add_sensed_object(self, sensed_object):
        self.sensed_objects.append(sensed_object)
        #self.sensed_objects(sensed_object)

    def add_name(self, name):
        self.name = name

    def build(self):
        return MotionTraceObject(self.inference_result, self.sensed_objects, self.name)


class AgentBuilder:
    def __init__(self):
        self.inference_result = None    
        self.sensed_objects = []
        self.name = None

    def set_inference_result(self, inference_result):
        self.inference_result = inference_result

    def add_sensed_object(self, sensed_object):
        self.sensed_objects.append(sensed_object)
        #self.sensed_objects(sensed_object)

    def add_name(self, name):
        self.name = name

    def build(self):
        return AgentObject(self.inference_result, self.sensed_objects, self.name)
    


    class GeoDataFrameBuilder:
        def __init__(self):
            self.data = {}      # Dictionary to store attribute data
            self.geometry = []  # List to store geometry objects


        def add_data(self, column_name, values):
            self.data[column_name] = values
            return self  # Return the builder instance to allow method chaining
            

        def add_geometry(self, geometry):
            self.geometry.append(geometry)
            return self  # Return the builder instance to allow method chaining
        
        
        def build(self):
            gdf = gpd.GeoDataFrame(self.data, geometry=self.geometry)
            return gdf


