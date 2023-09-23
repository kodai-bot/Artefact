from Archae_Objects.ArchaeObj_Base_Class import *


class SensedObjectBuilder:
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
        return SensedObject(self.data, self.name, self.sensed_position, self.incept_position, self.destruct_position)
    




class InferredObjectBuilder:
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
        return InferredObject(self.inference_result, self.sensed_objects, self.name)


