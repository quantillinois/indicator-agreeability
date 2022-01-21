"""Simple module that should pass the pylint testcase for sure."""


class Keep:
    """Simple test class to test out basic Git workflows."""

    def __init__(self) -> None:
        """Initialize the class"""
        self.message = ""
        self.first_number = 0
        self.second_number = 0

    def say_hello(self, message):
        """Says Hello to the function caller

        Returns:
            str: The hello world message
        """
        self.message = message
        return "Hello" + message

    def add_numbers(self, first_number, second_number):
        """Adds two numbers

        Args:
            a (Int): The first number
            b (Int): The second number

        Returns:
            Int: The sum of the two numbers
        """
        self.first_number = first_number
        self.second_number = second_number
        return first_number + second_number
