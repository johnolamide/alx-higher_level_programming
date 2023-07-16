# 0x0C-Python-Almost-a-Circle

## Task 0
- [x] `/tests`
> All your files, classes and methods must be unit tested and be PEP 8 validated.

## Task 1
- [x] `models/base.py`
> Write the first class `Base`

## Task 2
- [x] `models/rectangle.py`
> Write the class `Rectangle` that inherits from `Base`

## Task 3
- [x] `models/rectangle.py`
> Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

## Task 4
- [x] `models/rectangle.py`
> pdate the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the Rectangle instance.

## Task 5
- [x] `models/rectangle.py`
> Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character # - you don’t need to handle x and y here.

## Task 6
- [x] `models/rectangle.py`
> Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

## Task 7
- [x] `models/rectangle.py`
> Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character # by taking care of x and y

## Task 8
- [x] `models/rectangle.py`
> Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:

## Task 9
- [x] `models/rectangle.py`
> Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:

## Task 10
- [x] `models/square.py`
> Write the class `Square` that inherits from `Rectangle`

## Task 11
- [x] `models/square.py`
> Update the class `Square` by adding the public getter and setter `size`

## Task 12
- [x] `models/square.py`
> Update the class Square by adding the public method `def update(self, *args, **kwargs)` that assigns attributes:

## Task 13
- [ ] `models/rectangle.py`
> Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a Rectangle

## Task 14
- [ ] `models/square.py`
> Update the class Square by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`

## Task 15
- [ ] `models/bae.py`
> Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of list_dictionaries

## Task 16
- [ ] `models/base.py`
> Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file

## Task 17
- [ ] `models/base.py`
> Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`

## Task 18
- [ ] `models/base.py`
> Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set

## Task 19
- [ ] `models/base.py`
> Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances
