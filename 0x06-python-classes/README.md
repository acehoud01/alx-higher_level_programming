# 0x06 Python - Classes

## Overview

This module, 0x06 Python - Classes, introduces the fundamental concepts of Object-Oriented Programming (OOP) in Python. The focus is on understanding classes, instances, methods, and attributes, along with more advanced topics like inheritance and polymorphism. Through a series of tasks, learners will apply these concepts by creating their own classes and interacting with objects in Python.

## Objectives

- To understand and apply the principles of Object-Oriented Programming in Python.
- To learn how to define and use classes in Python.
- To explore the concepts of instance attributes, methods, and class attributes.
- To understand and implement inheritance and polymorphism.
- To gain familiarity with the `self` and `__init__` method in class definitions.
- To practice creating and working with instances of classes.

## Prerequisites

Before starting with this module, you should have a basic understanding of Python syntax and control structures. Familiarity with functions and modules in Python will also be beneficial.

## Contents

This module includes the following files and tasks:

- **0-square.py** - Defines an empty class Square that defines a square.
- **1-square.py** - Expands on the previous task by adding a private instance attribute `size`.
- **2-square.py** - Further improves the Square class to handle errors and validations for the `size` attribute.
- **3-square.py** - Implements a method to calculate the area of the square.
- **4-square.py** - Adds getter and setter methods for the `size` attribute to safely assign values.
- **5-square.py** - Enhances the Square class by adding a method to print the square using the `#` character.
- **6-square.py** - Introduces a position attribute with getter and setter, expanding the functionality to adjust the square's position.
- **100-singly_linked_list.py** - An advanced task that involves creating a SinglyLinkedList class with specific attributes and methods.
- **101-square.py** - Enhances the Square class to print its position when printed.
- **102-square.py** - Adds functionality to compare two Square instances based on their area.
- **103-magic_class.py** - An advanced task that requires recreating a bytecode representation of a Python class that involves mathematical operations.

## Requirements

- All your files should end with a new line.
- Your code should use the `pycodestyle` (version 2.5.*).
- All your files must be executable.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- All your files should start by including a comment explaining the task.
- All your classes should use the `class` description: `class ClassName:`.

## Testing

Your code will be tested using `unittests`. It's important to follow the instructions for each task and ensure your code passes all the tests. To run the tests, use the following command:

```sh
python3 -m unittest discover tests

