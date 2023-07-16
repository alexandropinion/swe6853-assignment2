#!/usr/bin/env python3
__NAME__ = "Pinion, Alexandro"
__EMAIL__ = "apinion1@students.kennesaw.edu"
__DESC__ = "Assignment 2 - Design Patterns - SWE6853 - Summer2023"

#: Imports
from abc import ABC, abstractmethod

#: Classes
class Graduate(ABC): # ABSTRACT FACTORY
    """
    The methods for producing the linked goods are declared in this interface or abstract class. 
    Within a product family, it offers a standard interface for the creation of objects of various types.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str
        self.features: list

    # Interface
    @abstractmethod
    def CreateStudent(self):
        pass

    # Interface 
    @abstractmethod
    def QueryStudent(self):
        pass

class Undergraduate(ABC): # ABSTRACT PRODUCT
    """
    These are the abstract classes or interfaces that list the common methods that 
    every product in a family ought to implement. 
    A separate category of product is represented by each abstract good.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str
        self.features: list

    @abstractmethod
    def CreateStudent(self):
        pass

    @abstractmethod
    def QueryStudent(self):
        pass


class National(Graduate): # CONCRETE PRODUCT
    """
    These are how the abstract products are really put into practice. 
    Each concrete product gives the methods described in the associated abstract product 
    a particular implementation.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str
        self.features: list

    def CreateStudent(self):
        self.name: str = "National"
        self.type: str = "Graduate"
        self.features: list = [self.name,  self.type]

    def QueryStudent(self):
        return ["National", "Graduate"]


class International(Graduate): # CONCRETE PRODUCT
    """
    These are how the abstract products are really put into practice. 
    Each concrete product gives the methods described in the associated abstract product 
    a particular implementation.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str
        self.features: list

    def CreateStudent(self):
        self.name: str = "International"
        self.type: str = "Graduate"
        self.features: list = [self.name,  self.type]

    def QueryStudent(self):
        return ["International", "Graduate"]

class National(Undergraduate): # CONCRETE PRODUCT
    """
    These are how the abstract products are really put into practice. 
    Each concrete product gives the methods described in the associated abstract product 
    a particular implementation.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str
        self.features: list

    def CreateStudent(self):
        self.name: str = "National"
        self.type: str = "Undergraduate"
        self.features: list = [self.name,  self.type]

    def QueryStudent(self):
        return [ "National", "Undergraduate"]


class International(Undergraduate): # CONCRETE PRODUCT
    """
    These are how the abstract products are really put into practice. 
    Each concrete product gives the methods described in the associated abstract product 
    a particular implementation.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str
        self.features: list

    def CreateStudent(self):
        self.name: str = "International"
        self.type: str = "Undergraduate"
        self.features: list = [self.name,  self.type]

    def QueryStudent(self):
        return ["International", "Undergraduate"]



class Students(ABC): # ABSTRACT FACTORY
    """
    The methods for producing the linked goods are declared in this interface or abstract class. 
    Within a product family, it offers a standard interface for the creation of objects of various types.
    """

    @abstractmethod
    def CreateStudent(self):
        pass

    @abstractmethod
    def QueryStudent(self):
        pass

class StudentInternational(Students): # CONCRETE FACTORY
    """
    These are how the abstract factory is implemented. 
    Each concrete manufacturing facility offers a unique method for producing goods from a certain family.
    """
    
    def CreateStudent(self):
        return International()

    def QueryStudent(self):
        return International.QueryStudent(self)

class StudentNational(Students): # CONCRETE FACTORY
    """
    These are how the abstract factory is implemented. 
    Each concrete manufacturing facility offers a unique method for producing goods from a certain family.
    """
    def CreateStudent(self):
        return National()

    def QueryStudent(self):
        return National.QueryStudent(self)
    

def client(): # An implementation of the client utilizing the abstract factory and abstract product(s).
    # Client can use the abstract factory to create students or query existing students.
    for factory in (StudentInternational(), StudentNational()):
        productA = factory.CreateStudent()
        productB = factory.QueryStudent()
        new_student = productA.QueryStudent()
        print(f"This is factory # {factory.__class__}\nProduct A: {productA}\nProductB: {productB}\nNew Student: {new_student}\n\n")


if __name__ == "__main__":
    client()