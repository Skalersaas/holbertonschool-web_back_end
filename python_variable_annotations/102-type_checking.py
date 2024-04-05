#!/usr/bin/env python3
''' Description: Type-annotated function safe_first_element
    that takes a list lst as argument
    and Checks if list exist, if yes returns first element.
    Arguments: lst: Sequence[Any]
'''


def zoom_array(lst: tuple, factor: int = 2) -> list:
    """Zoom your camera"""
    zoomed_in: list = [item for item in lst for i in range(factor)]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
