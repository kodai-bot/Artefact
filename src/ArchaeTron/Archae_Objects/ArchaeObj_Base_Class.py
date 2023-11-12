from abc import ABC, abstractmethod
import math


# Abstract archaeological object base class

class ArchaeoObject(ABC):
    def __init__(self, name, object_type):
        self.name = name
        self.object_type = object_type  # Attribute to declare sensed or inferred

    @abstractmethod
    def operation(self):
        pass




# Concrete implementations of ArchaeObject subclasses

class ArchaeoSiteObject(ArchaeoObject):
    def __init__(self, name, object_type):
        self.name = name
        self.object_type = object_type  # Attribute to declare sensed or inferred
        self.children = []
        self.state_vector = {
            'RA': None,
            'Declination': None,
            'Distance': None
        }



    # Method to print the object tree

    def operation(self):
        print(f"Object: {self.name} - Type: {self.object_type}")
        for child in self.children:
            child.operation()
      

    # Functions to add and remove objects from the tree

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)


    # Functions to return number of objects in the tree and the depth of the tree

    def count_objects(self):
        count = 1  # Count the current object
        for child in self.children:
            count += child.count_objects()  # Recursively count objects in children
        return count
    
    def find_depth(self):
        if not self.children:
            return 1  # Leaf node
        else:
            max_child_depth = max(child.find_depth() for child in self.children)
            return max_child_depth + 1


    # Setters for object attributes

    def set_name(self, name):
        self.name = name
        return self

    def set_object_type(self, object_type):
        self.object_type = object_type
        return self


    

    def set_geo_location(self, latitude, longitude):
    # Location of object in coordinate space on earths surface.
        self.latitude = latitude
        self.longitude = longitude
        return self

    def set_altitude(self, altitude):
        self.altitude = altitude    # Altitude of object in meters above sea level
        return self

    def set_depth(self, depth):
        self.depth = depth    # Depth of object in meters below surface
        return self
    
    def set_dimensions(self, geometry):
        self.geometry = [geometry]    # Dimensions of object
        return self

    def set_material(self, material):
        self.material = material     # Material of object
        return self

    def set_volume(self, volume):
        self.volume = volume    # Volume of object in cubic meters
        return self

    def set_symmetry_type(self, symmetry_type):
        self.symmetry_type = symmetry_type    # Symmetry type of object radial, bilateral, etc.
        return self

    def set_tesselation(self, tesselation):
        self.tesselation = tesselation    # Tesselation of object
        return self

    def set_colour(self, colour):
        self.colour = colour    # Colour of object
        return self
        

    

    def set_soil_type(self, soil_type):
        self.soil_type = soil_type    # Soil type at object location
        return self

    def set_land_cover(self, land_cover):
        self.land_cover = land_cover    # Land cover type at object location
        return self

    def set_geology(self, geology):
        self.geology = geology    # Geology type at object location
        return self
        


    # Time attributes

    def set_incept_date(self, incept_date):
        self.incept_date = incept_date     # Date of creation, can be inferred or a default value for the class
        # of object
        # Convert dates to distance from present. In practice just the number of years from present.
        return self


    def set_destruct_date(self, destruct_date):
        self.destruct_date = destruct_date     # Date of destruction, can be inferred or a default value for the class
        # Convert dates to distance from present. In practice just the number of years from present.
        return self


    def update_state_vector(self, ra, declination, distance):
        self.state_vector['RA'] = ra
        self.state_vector['Declination'] = declination
        self.state_vector['Distance'] = distance
        return self

    
    def get_state_vector(self):
        return self.state_vector

    
    # Returns a vector based on latitude and longitude perpindicular to the earths surface.
    def get_RA_Dec(self):
        ra, declination = postionCalculator(self.latitude, self.longitude)
        return ra, declination
    



        # Assembly index of object is the shortest number steps required to assemble the object from basic 
        #building blocks, Copy number is the total number of copies of the object known to exist.This returns 
        # a values measuring the complexity and frequency of the object and therefore its likelihood to be the result of selection. Applications in SETI are likely.
        # Refer to http://doi.org/10.1038/s41586-023-06600-9

    def calculate_assembly_index(self, assembly_index, copy_number):

        self.assembly_index = assembly_index    # Assembly index of object
        self.copy_number = copy_number      # Number of copies of object in ensemble


        # Calculate objects assembly number, a measure of the complexity of the object and the likelihood of it
        #being the result of a selection process.

        object_assembly_index = math.e ** self.find_depth() * (copy_number -1) / self.count_objects()
        
        return object_assembly_index

        # Assembly index is a measure of the complexity of an object


    

        # Concrete implementations of Sensed and Inferred subclasses

        # uaon = Universal Archaeological Object Number



