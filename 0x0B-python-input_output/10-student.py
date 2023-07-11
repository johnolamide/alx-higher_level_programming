#!/usr/bin/python3
""" Module contains class definition of Student
"""


class Student:
    """
        Student: defines a student class
        Args:
            first_name (str):
            last_name (str):
            age (int):
        Methods:
            __init__: initializes the student class
            __str__: string representation of an instance
            first_name: getter for the first name
            first_name(value): setter for the first name
            last_name: getter for the last name
            last_name(value): setter for the last name
            age: getter for the age
            age(value): getter for the age
            to_json: retrieves a dictionary representation
            of a student instance
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes the Student class
            Args:
                first_name (str): student first name
                last_name (str): student last name
                age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """ String representation of a Student instance
        """
        pass

    @property
    def first_name(self):
        """ Getter for the first_name attribute
            Returns:
                value of first_name
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """ Setter for the first_name attribute
            Args:
                value: value for first_name
        """
        self.__first_name = value

    @property
    def last_name(self):
        """ Getter for the last_name attribute
            Returns:
                value of last_name
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """ Setter for the last_name attribute
            Args:
                value: value for last_name
        """
        self.__last_name = value

    @property
    def age(self):
        """ Getter for the age attribute
            Returns:
                value of age
        """
        return self.__age

    @age.setter
    def age(self, value):
        """ Setter for the age attribute
            Args:
                value: value for age
        """
        self.__age = value

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in
                    attrs if hasattr(self, attr)}


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
