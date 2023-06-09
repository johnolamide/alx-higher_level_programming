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
            reload_from_json: replaces all attributes of the Studen
            instance
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

    def reload_from_json(self, json):
        """ Replaces all attributes of the students instance
            Args:
                json: json text file
        """
        for key, value in json.items():
            setattr(self, key, value)


if __name__ == "__main__":
    import os
    import sys

    Student = __import__('11-student').Student
    read_file = __import__('0-read_file').read_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    new_student_1.reload_from_json(j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
