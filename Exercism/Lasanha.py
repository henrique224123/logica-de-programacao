# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer


# TODO: define the 'bake_time_remaining()' function
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time


def preparation_time_in_minutes(layers):
    """Calculate the bake time remaining.

        :param layers: int baking time already elapsed.
        :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
        """
    return layers * 2


def elapsed_time_in_minutes(layer, time_oven):
    """Calculate the bake time remaining.

        :param layer: int baking time already elapsed.
        :param time_oven: int baking time already elapsed.
        :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
        """
    return preparation_time_in_minutes(layer) + time_oven


    pass

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here

# TODO: define the 'elapsed_time_in_minutes()' function
