# Sure, here is an example of an abstract factory that produces two types of objects, Sensed and Inferred, 
# which are derived from two abstract classes called Sensed and Inferred:

from abc import ABC, abstractmethod
from ArchaeObj_Base_Class import *


class SensedFactory(ABC):
   @abstractmethod
   def create_sensed(self):
       pass

class InferredFactory(ABC):
   @abstractmethod
   def create_inferred(self):
       pass

class ConcreteSensedFactory(SensedFactory):
   def create_sensed(self):
       return Sensed()

class ConcreteInferredFactory(InferredFactory):
   def create_inferred(self):
       return Inferred()



