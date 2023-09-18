# abstract factory that produces two types of objects, Sensed and Inferred, 
# and concrete factories derived from two abstract classes called Sensed and Inferred:

from abc import ABC, abstractmethod
from Archae_Objects.ArchaeObj_Base_Class import *

class SensedFactory(ABC):
    @abstractmethod
    def create_sensed(self, obj_name):
        pass

class InferredFactory(ABC):
    @abstractmethod
    def create_inferred(self, inf_result, sensed_obj, name):
        pass

# Concrete Factory classes.

class ConcreteSensedFactory(SensedFactory):
    def create_sensed(self, obj_name):
        return SensedObject(obj_name)

class ConcreteInferredFactory(InferredFactory):
    def create_inferred(self, inf_result, sensed_obj, name):
        return InferredObject(inf_result, sensed_obj, name)




