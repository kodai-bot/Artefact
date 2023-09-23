from abc import ABC, abstractmethod

# Abstract archaeological object base classes

class Sensed(ABC):
    def __init__(self, name):
        self.sensed_data = None
        self.name = name
        self.sensed_position = None
        self.incept_position = None
        self.destruction_position = None
    


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
        self.sensed_position = None
        self.incept_position = None
        self.destruction_position = None


    def sense(self):
        self.sensed_data = "Sensed data"

        

class InferredObject(Inferred):
    def __init__(self, inf_result, sensed_obj, name):
        self.inf_result = inf_result
        self.sensed_obj = sensed_obj
        self.name = name

    def infer(self):
        pass


class InferredState(self, sensed_obj, state):
    def __init__(self, sensed_obj, name):
        self.sensed_obj = sensed_obj
        self.name = name
        self.state = state

    def infer(self):
        pass

class InferredMotionPattern(self, sensed_obj, motion_pattern):
    def __init__(self, sensed_obj, name):
        self.sensed_obj = sensed_obj
        self.name = name
        self.motion_pattern = motion_pattern

    def infer(self):
        pass


class InferredAgent(self, sensed_obj, agent):
    def __init__(self, sensed_obj, name):
        self.sensed_obj = sensed_obj
        self.name = name
        self.agent = agent

    def infer(self):
        pass