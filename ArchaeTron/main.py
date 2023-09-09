

from Archae_Object_Factory import *

def main():
   # Create concrete archaeological object factories

   sensed_factory = ConcreteSensedFactory()
   inferred_factory = ConcreteInferredFactory()

   # Create Archaeological Objects of either class using the factory

   sensed_object = sensed_factory.create_sensed()
   inferred_object = inferred_factory.create_inferred()

 # view objects structure

   print(sensed_object.__dict__)
   print(inferred_object.__dict__)
   print(sensed_object.__class__)
   print(inferred_object.__class__)

if __name__ == "__main__":
   main()