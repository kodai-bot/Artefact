# abstract factory that produces two types of objects, Sensed and Inferred, 
# and concrete factories derived from two abstract classes called Sensed and Inferred:

from abc import ABC, abstractmethod
from Archae_Objects.ArchaeObj_Base_Class import *
from Builders.ObjectBuilder import *


class SensedFactory(ABC):
    @abstractmethod
    def create_sensed(self, obj_name):
        pass

    @abstractmethod
    def create_sensed_builder(self):
        return SensedObjectBuilder()

class InferredFactory(ABC):
    @abstractmethod
    def create_inferred(self, obj_name):
        pass

    @abstractmethod
    def create_inferred_builder(self):
        return InferredObjectBuilder()
    

# Concrete Factory classes.

class ConcreteSensedFactory(SensedFactory):

    def create_sensed(self, obj_name):
        return Sensed(obj_name)
    
    #def create_sensed_builder(self):
    #   return SensedObjectBuilder()

class ConcreteInferredFactory(InferredFactory):

    def create_inferred(self, obj_name):
        return Inferred(obj_name)
    
    #def create_inferred_builder(self):
    #    return InferredObjectBuilder()
    




