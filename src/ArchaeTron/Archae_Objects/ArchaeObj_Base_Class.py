from abc import ABC, abstractmethod

# Abstract archaeological object base classes

class ArchaeObject(ABC):
    def __init__(self):
        self.data = None
        self.name = None
        self.number = None
        self.sensed_position = None
        # self.incept_position = None
        # self.destruction_position = None

    @abstractmethod
    def clone(self):
        pass




class Sensed(ArchaeObject):
    def __init__(self):
        self.sensed_data = None
        self.name = None
        self.number = None
        self.sensed_position = None
        self.incept_position = None
        self.destruction_position = None
    
    @abstractmethod
    def sense(self, sensed_data):
        pass



class Inferred(ArchaeObject):
    def __init__(self, inf_result, sensed_obj, name):
        self.inf_result = inf_result
        self.sensed_obj = sensed_obj
        self.name = name
    
    @abstractmethod
    def infer(self):
        pass



# Concrete implementations of Sensed and Inferred subclasses

class ArchObject(Sensed):
    def __init__(self, sensed_obj, name):
        self.sensed_obj = sensed_obj
        self.name = name
        self.agent = agent
        self.symmetry = symmetry

    def sense(self, sensed_data):
        self.sensed_data = sensed_data
        return self.sensed_data
    
    def clone(self):
        return self.__class__(self.sensed_obj, self.name, self.agent, self.symmetry)    
    
    
   
    

# uaon = Universal Archaeological Object Number

class ArchObject(Inferred):
    def __init__(self, uaon, name):
        self.uaon = uaon
        self.name = name
        self.agent = None
        self.symmetry = None

    def infer(self):
        self.inference_result = inference_result
        return self.inference_result
    
    def clone(self):
        return self.__class__(self.uaon, self.name, self.agent, self.symmetry)

