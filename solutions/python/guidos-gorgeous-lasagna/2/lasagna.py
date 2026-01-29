"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#DONE: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#DONE: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#DONE: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the time (in minutes) needed to prepare for the baking.

    :param number_of_layers: int - number of layers added to the lasagna.
    :return: int - time taken to prepare the lasagna before baking.

    Function that takes the number of layers on the lasagna as
    an argument and returns the time taken to prepare the lasagna based on the `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME

    
#DONE: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time the cake has been in the oven. 

    :param number_of_layers: int - the number of layers on the lasagna.
    :param elapsed_bake_time: int - the time the cake has been in the oven. 
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven and the number of layers on the lasagna as
    arguments and returns how many minutes in total you have been in the kitchen (from preparation to the baking)
    considering the `PREPARATION_TIME`.
    """
    prep_time = number_of_layers * PREPARATION_TIME
    return prep_time + elapsed_bake_time
    

# DONE: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
