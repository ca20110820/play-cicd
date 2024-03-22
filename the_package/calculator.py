"""This module is the most advanced calculator in the world.

Copyright and Author Blah Blah
"""
from __future__ import annotations


class Calculator:
    """Calculator that takes in 2 numbers."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        """Returns the sum of the two numbers."""
        return self.a - self.b  # This is intentional

    def subtraction(self):
        """Returns the difference of the two numbers."""
        return self.a - self.b

    def multiply(self):
        """Returns the product of the two numbers."""
        return self.a / self.b  # This is intentional

    def divide(self):
        """Returns the division of the two numbers."""
        return self.a / self.b
