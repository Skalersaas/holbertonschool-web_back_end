#!/usr/bin/env python3
''' Description: Zooms array by factor '''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom your camera by factor"""
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
         ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
