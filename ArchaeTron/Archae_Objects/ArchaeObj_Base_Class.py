from abc import ABC, abstractmethod

# Abstract archaeological object base classes

class Sensed(ABC):
    def __init__(self, name):
        self.sensed_data = None
        self.name = name

    @abstractmethod
    def sense(self, sensed_data):
        pass

class Inferred(ABC):
    def __init__(self, inf_result, sensed_obj, name):
        self.inf_result = inf_result
        self.sensed_obj = sensed_obj
        self.name = name
    

    @abstractmethod
    def infer(self):
        pass

# Concrete implementations of Sensed and Inferred

class SensedObject(Sensed):
    def __init__(self, name):
        self.sensed_data = None
        self.name = name

    def sense(self):
        self.sensed_data = "Sensed data"

class InferredObject(Inferred):
    def __init__(self, inf_result, sensed_obj, name):
        self.inf_result = inf_result
        self.sensed_obj = sensed_obj
        self.name = name

    def infer(self):
        pass


