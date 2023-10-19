# abstract factory that produces two types of objects, Sensed and Inferred, 
# and concrete factories derived from two abstract classes called Sensed and Inferred:

from abc import ABC, abstractmethod
from Archae_Objects.ArchaeObj_Base_Class import *
from Builders.ObjectBuilder import *


class ArchObjectFactory(ABC):
    
    @abstractmethod
    def create_sensed_builder(self):
        pass
    
    @abstractmethod
    def create_inferred_builder(self):
        pass

    @abstractmethod
    def create_GeoDataFrameBuilder(self):
        pass

    

# Concrete Factory classes.

class ConcreteObjectFactory(ArchObjectFactory):

    def create_sensed(self, obj_name):
        return Sensed(obj_name)
    
    def create_inferred(self, obj_name):
        return Inferred(obj_name)
    

    # Complex Object builders

    def create_sensed_builder(self, obj_name):
        return SensedObjectBuilder()
    
    def create_inferred_builder(self, obj_name):
       return InferredObjectBuilder()
    
    def create_GeoDataFrameBuilder(self):
        return GeoDataFrameBuilder()    
    




