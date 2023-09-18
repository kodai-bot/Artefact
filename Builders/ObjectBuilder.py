

class SensedObjectBuilder:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def build(self):
        return SensedObject(self.data)






class InferredObjectBuilder:
    def __init__(self):
        self.inference_result = None
        self.sensed_objects = []

    def set_inference_result(self, inference_result):
        self.inference_result = inference_result

    def add_sensed_object(self, sensed_object):
        self.sensed_objects.append(sensed_object)

    def build(self):
        return InferredObject(self.inference_result, self.sensed_objects)


