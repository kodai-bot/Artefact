from abc import ABC, abstractmethod

# Abstract archaeological object base classes

class Sensed(ABC):
    @abstractmethod
    def sense(self):
        pass

class Inferred(ABC):
    def __init__(self, sensed_obj):
        self.sensed_obj = sensed_obj

    @abstractmethod
    def infer(self):
        pass

# Concrete implementations of Sensed and Inferred

class Sensed:
   def __init__(self):
       self.sensed_data = None

   def sense(self):
       self.sensed_data = "Sensed data"

class Inferred:
   def __init__(self):
       self.inferred_data = None

   def infer(self):
       self.inferred_data = "Inferred data"


