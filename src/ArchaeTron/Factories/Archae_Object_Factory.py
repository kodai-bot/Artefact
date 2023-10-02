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

    

# Concrete Factory classes.

class ConcreteObjectFactory(ArchObjectFactory):

    def create_sensed(self, obj_name):
        return Sensed(obj_name)
    




    def create_sensed_builder(self, obj_name):
        return SensedObjectBuilder(obj_name)
    
    def create_inferred_builder(self, obj_name):
       return InferredObjectBuilder()
    


class ConcreteMotionTraceFactory(ArchObjectFactory):

    def create_inferred(self, trace_name):
        return Inferred(trace_name)
    
    def create_motion_trace_builder(self):
        return MotionTraceBuilder()
    

class ConcreteAgentFactory(ArchObjectFactory):

    def create_agent(self, agent_name):
        return Inferred(obj_name)
    
    def create_agent_builder(self):

        return MotionTraceBuilder()


