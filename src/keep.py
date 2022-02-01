"""Simple module that should pass the pylint testcase for sure."""

import pandas as pd


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
    '''
    Input - 
    price_array = [5.093202617298384, 5.1186766373255494, 5.173893746495927, 5.295009073341559, 5.399191447443256, 5.351825535182657, 5.408024435253786, 5.405247024879783, 5.405073037988975, 5.432671259949622]
    smoothing = 2 
    window_size = 20

    Output = 
    ema array
    '''

    def exponential_moving_average(self, price_array, smoothing, window_size):
        #df = pd.DataFrame(price_array, columns=['price'])
        # print(df)
        ema = []
        ema_value = 0
        for price in price_array:
            if ema_value == 0:
                ema_value = price
            else:
                ema_value = smoothing*price+(1-smoothing)*ema_value
            ema.append(ema_value)
        # print(ema)
        return ema
